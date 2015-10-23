#
# spec file for package fdupes (Version 1.40)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           fdupes
URL:            http://premium.caribe.net/~adrian2/fdupes.html
Group:          Productivity/Archiving/Compression
Summary:        Identifying or deleting duplicate files
Version:        1.40
Release:        %{?release_prefix:%{release_prefix}.}42.8.%{?dist}%{!?dist:tizen}
VCS:            external/fdupes#submit/trunk/20121019.103317-0-g6bdbd819e2f065d336b7a7e13e2c5636e304fc34
License:        X11/MIT
Source0:        %name-%{version}.tar.bz2
Source1:        macros.fdupes
Patch0:         %name.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories



Authors:
--------
    Adrian Lopez <adrian2@caribe.net>

%prep
%setup -q
%patch0

%build
make

%install
install -D -m755 fdupes $RPM_BUILD_ROOT/usr/bin/fdupes
install -D -m644 fdupes.1 $RPM_BUILD_ROOT/usr/share/man/man1/fdupes.1
install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/etc/rpm/macros.fdupes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc CHANGES
%{_prefix}/bin/fdupes
%{_mandir}/*/*
/etc/rpm

%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121019.103317 
- PROJECT: external/fdupes
- COMMIT_ID: 6bdbd819e2f065d336b7a7e13e2c5636e304fc34
- PATCHSET_REVISION: 6bdbd819e2f065d336b7a7e13e2c5636e304fc34
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103429
- PATCHSET_REVISION: 6bdbd819e2f065d336b7a7e13e2c5636e304fc34
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 1.40
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Tue Sep  1 2009 Anas Nashif <anas.nashif@intel.com> - 1.40
- Initial import into Moblin
* Thu Sep  6 2007 mls@suse.de
- do not hardlink empty files in %%%%fdupes macro
* Wed Sep  5 2007 nadvornik@suse.cz
- support filenames with spaces in %%%%fdupes macro [#307727]
* Tue May 15 2007 coolo@suse.de
- add an RPM macro to make use of it in spec files
* Thu Nov 16 2006 dmueller@suse.de
- Initial package (1.40)
