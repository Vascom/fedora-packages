#!/usr/bin/env perl
# Generates a beautiful HTML table from the table_content file
use constant GIT_URL => "http://pkgs.fedoraproject.org/cgit/";
use constant PROJECT_URL => "https://apps.fedoraproject.org/packages/";
use constant BUGZILLA_URL => "https://bugzilla.redhat.com/show_bug.cgi?id=";
open(FILE, "table_content");

print "<table>\n" . 
        "  <tr>\n" .
            "    <th>Package Name</th>\n" .
            "    <th>Version</th>\n" .
            "    <th>Status</th>\n" .
            "    <th>Ticket</th>\n" .
            "    <th>Git</th>\n" .
            "    <th>Info</th>\n" .
        "  </tr>\n";

while (<FILE>) {
  if ($_ =~ m/\|\s*([^| ]+)\s*\|\s*([0-9.]+)\s*\|\s*([A-Z]+)\s*\|\s*([0-9]+)\s*\|\s*([^| ]+)\s*\|\s*([^|]+)\s*\|$/) {
    my ($package_name, $version, $status, $ticket, $git, $info) = ($1, $2, $3, $4, $5, $6);
    print "  <tr>\n" .
            "    <td><a href=\"" . PROJECT_URL . "$package_name\">$package_name</a></td>\n" .
            "    <td>$version</td>\n" .
            "    <td>$status</td>\n";

    print "    <td>";
    if ($ticket =~ m/None/) {
      print "<a href=\"" . BUGZILLA_URL . "$ticket\">#$ticket</a>";
    }

    print "</td>\n    <td>";
    if ($git =~ m/Fedora/) {
      print "<a href=\"" . GIT_URL . "$package_name\">$package_name</a>";
    }

    print "</td>\n    <td>";

    print "</td>\n    <td>";
    if (!($info =~ m/None.*/)) {
      print "$info";
    }

    print "</td>\n  </tr>\n"; 
  }
}

print "</table>\n";

