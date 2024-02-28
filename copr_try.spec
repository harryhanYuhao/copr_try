###############################################################################
# Spec file for Utils
################################################################################
# Configured to be built by user hhyh or other non-root user
################################################################################
#
Summary: Utility scripts for testing RPM creation
Name: copr_try
Version: 1.0.2
Release: 1
License: GPLv3
URL: http://www.both.org
Group: System
Packager: David Both
Requires: bash
Requires: screen
Requires: mc
Requires: dmidecode
BuildRoot: ~/rpmbuild/
BuildArch: x86_64

# Build with the following syntax:
# rpmbuild --target noarch -bb utils.spec

%description
A collection of utility scripts for testing RPM creation.

%prep
################################################################################
# Create the build tree and copy the files from the biblioteca/copr_try directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/usr/local/share/copr_try

cp /home/hhyh/biblioteca/copr_try/src/* $RPM_BUILD_ROOT/usr/local/bin
cp /home/hhyh/biblioteca/copr_try/LICENSE $RPM_BUILD_ROOT/usr/local/share/copr_try
cp /home/hhyh/biblioteca/copr_try/copr_try.spec $RPM_BUILD_ROOT/usr/local/share/copr_try

exit

%files
%attr(0744, root, root) /usr/local/bin/*
%attr(0644, root, root) /usr/local/share/copr_try/*

%pre

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT/usr/local/bin
rm -rf $RPM_BUILD_ROOT/usr/local/share/copr_try

%changelog
* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk> 1.0.2-1
- init (s2162783@ed.ac.uk)

* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk>
- init (s2162783@ed.ac.uk)

* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk> 1.0.0-1
- Init

* Wed Feb 28 2024 Harry Yuhao Han <s2162783@ed.ac.uk> 1.0.1-1
- new package built with tito

* Wed Aug 29 2018 Your Name <Youremail@yourdomain.com>
  - The original package includes several useful scripts. it is
    primarily intended to be used to illustrate the process of
    building an RPM.
