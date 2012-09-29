#!/usr/bin/env perl
#
# Copyright (c) 2012, Minh Ngo <nlminhtl@gmail.com>
#
# This code is distributed under Artistic License 1.0.
# Look http://www.perlfoundation.org/artistic_license_1_0
# for more info.
# This script is used for package git repository sources
# into a single source archive.
#
use Git::PurePerl;
use Archive::Tar;
use IO::Compress::Bzip2;
use File::Path qw(remove_tree);
use File::Find;
use Cwd;
use Getopt::Long;

my $help = '';
my $url = '';
my $source_version = '';

sub print_help {
  print "Usage: ./source_archiver.pl [OPTION]\n" .
        "Example: ./source_archiver.pl --url=https://code.google.com/p/qxmpp/ --ver=0.7.3\n" .
        "Options:\n" .
        "\t--url\t\t\tvcs repository URL.\n" .
        "\t--ver\tsource archive version\n";
  exit;
};

if (@ARGV > 0) {
  GetOptions(
    'help|H' => \$help,
    'url=s' => \$url,
    'ver=s' => \$source_version,
  );
}

if ($help) {
  print_help;
}
elsif (!($url && $source_version)) {
  print "url and source_version are required!\n";
  exit;
}
elsif ($vcs && $vcs != "git") {
  print "non git vcs is not supported now.\n";
  exit;
}

my $current_dir = getcwd;

my $temp_dir = "/tmp/source_$$";
mkdir $temp_dir, 0700 or die "cannot create $temp_dir: $!";
chdir $temp_dir or die "cannot change directory to $temp_dir: $!";
system "git", "clone", $url;

my $project_name = $url;
$project_name =~ s/.*\/(\w+)\/$/$1/;
print "project name: $project_name\n";
print "version: $source_version\n";

my $git = Git::PurePerl->new(
  directory => "$temp_dir/$project_name"
);

my $folder_name = $project_name . '-' . $source_version
;
my $hash = substr($git->master_sha1, 0, 7);
rename $project_name, $folder_name;
chdir "$temp_dir/$folder_name";
remove_tree(".git");
chdir $temp_dir;

@accum = ();
finddepth(\&wanted, ".");
sub wanted {
  push(@accum, $File::Find::name);
};

Archive::Tar->create_archive("$current_dir/$folder_name-" . $hash . ".tar.bz2", COMPRESS_BZIP2, @accum);
chdir $current_dir;
remove_tree($temp_dir);
