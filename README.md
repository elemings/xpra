
# Xpra 3
This document defines a build, install, and test procedure for Xpra 3 RPMs on RHEL 7 platforms.
This is a rough draft and has not yet been reviewed for correctness or completeness.

## RPM Build Primer
This section contains a brief overview of working with RPM files.

### Rebuilding RPMs From SRPMs
To rebuild an SRPM (Source RPM), execute an `rpmbuild --rebuild <SRPM-FILENAME>` command.  Example:
	`$ rpmbuild --rebuild foo.src.rpm`
The `-v` option is often added to many `rpmbuild` commands to produce more diagnostic output when errors occur.  Example:
	`$ rpmbuild -v --rebuild foo.src.rpm`

### Inspecting SRPMs
The following command will show all information and files contained in an SRPM.
	`$ rpm -qilpv foo.src.rpm`

### RPM Build Directory Trees
An RPM build directory tree (or "rpmbuild tree" for short) is simply an `rpmbuild` directory with a conventional set of subdirectories as shown in the following list.
`	rpmbuild/BUILD
	rpmbuild/BUILDROOT
	rpmbuild/RPMS/noarch
	rpmbuild/RPMS/x86_64
	rpmbuild/SOURCES
	rpmbuild/SPECS
	rpmbuild/SRPMS`
The subdirectory names for the `rpmbuild/RPMS` directory may vary depending on the target platform(s).  There is a small but useful utility called `rpmdev-setuptree` that is commonly used to create new rpmbuild trees.

### Extracting SRPMs
Extracting an SRPM is the same as "installing" it only it is always extracted into an `rpmbuild` directory tree.  This directory tree is specified by the `%_topdir` macro (which defaults to the `${HOME}/rpmbuild` directory when undefined) in your `.rpmmacros` configuration file.  If you want SRPMs installed somewhere other than `${HOME}/rpmbuild`, add the following line to your `${HOME}/.rpmmacros` file to define the %_topdir macro.
	`%_topdir	%{getenv:HOME}/some-other-place/rpmbuild`
If you use more than one rpmbuild tree, you can comment-out the ones you don't need.  Example:
	`#%_topdir	%{getenv:HOME}/some-other-place/rpmbuild`
	`%_topdir	/workspace/projects/%{getenv:LOGNAME}/rpmbuild`
Then just "install" the SRPM:
	`$ rpm -ivh foo.src.rpm`
You will find the SPEC file (probably named `foo.spec` in this case) in the `SPECS` subdirectory of the `rpmbuild` tree and source code (and any optional patches) in the `SOURCES` subdirectory.

### Building RPMs Using .spec Files
To build an RPM from its corresponding SPEC file, execute an `rpmbuild` command using the `-b` (and `-v`) options.  Example:
	`$ rpmbuild -v -ba --clean foo.spec`
The `a` argument in the `-b` option means build "all" files (i.e. a new SRPM file as well as the usual RPM files).


## Download Xpra 3 SRPMs
The Xpra 3 SRPM files can be downloaded from the Xpra web site at <https://xpra.org/dists/RedHat/7.7/SRPMS/>.  A BASH script for downloading these SRPM files is shown below.

    #!/bin/sh
    
    base_url=https://xpra.org/dists/RedHat/7.7/SRPMS
    
    # Latest versions of RHEL 7.7 packages from URL above.
    # Last updated: Wed Feb 05 08:00:29 MST 2020
    srpm_files=(
	    ffmpeg-xpra-4.2.2-2.el7_7.src.rpm
	    gstreamer1-plugin-timestamp-0.1.0-1.el7_7.src.rpm
	    gtkglext-1.2.0-22.el7_7.src.rpm
	    lame-3.100-1.el7_7.src.rpm
	    libfakeXinerama-0.1.0-3.el7_7.src.rpm
	    libmad-0.15.1b-3.el7_7.src.rpm
	    libvpx-xpra-1.8.1-1.el7_7.src.rpm
	    libwebp-xpra-1.0.3-1.el7_7.src.rpm
	    libyuv-0-0.35.20190401git4bd08cb.el7_7.src.rpm
	    lz4-1.8.3-1.el7_7.src.rpm
	    pangox-compat-0.0.2-1.el7_7.src.rpm
	    pygtkglext-1.1.0-27.xpra3.el7_7.src.rpm
	    python2-Cython-0.29.13-1.el7_7.src.rpm
	    python2-lz4-2.2.1-2.src.rpm
	    python2-netifaces-0.10.9-1.el7_7.src.rpm
	    python2-pillow-5.4.1-1.el7_7.src.rpm
	    python2-pycuda-2018.1.1-3.src.rpm
	    python2-pynvml-10.418.84-1.src.rpm
	    python2-pyopengl-3.1.1a1-10xpra1.el7_7.src.rpm
	    python2-pytools-2019.1.1-1.el7_7.src.rpm
	    python2-pyu2f-0.1.4-2.src.rpm
	    python2-rencode-1.0.6-1.xpra1.el7_7.src.rpm
	    python2-uinput-0.11.2-3.el7_7.src.rpm
	    python2-xxhash-1.4.1-1.el7_7.src.rpm
	    x264-xpra-20190929-1.el7_7.src.rpm
	    xorg-x11-drv-dummy-0.3.8-1.xpra2.el7_7.src.rpm
	    xpra-3.0.5-0.r24939xpra1.el7_7.src.rpm
	    yasm-1.3.0-1.el7_7.src.rpm
    )
    
    download_dir=${1:-~/Downloads/xpra}
    mkdir -p ${download_dir}
    
    for srpm_file in ${srpm_files[*]}
    do
      eval /usr/bin/curl -s -R ${base_url}/${srpm_file} -o \'${download_dir}/${srpm_file}\'
    done
    
    eval chmod 644 \'${download_dir}/*.src.rpm\' 2>/dev/null
    
    exit 0

These files should be downloaded to the `SRPMS` subdirectory in an `rpmbuild` tree.  Note that some of these SRPM files have been further refined for less common installs of RHEL 7 OS (e.g. when security profiles are enabled such as FIPS) and are thus not used in the build procedure itself but still have historical value in that they can be used to compare and contrast changes made in their more refined counterparts.
The refined Xpra 3 SRPMS can be found in the GitHub repostory located at [https://github.com/elemings/xpra-rpmbuild.git](https://github.com/elemings/xpra-rpmbuild.git).  You can use the rpmbuild tree in this Git repo or copy these SRPM files to your own `rpmbuild` tree.

## Building Xpra 3 RPMs
This section describes the build procedure for building Xpra 3 RPM files for the RHEL 7 x86_64 target platform.

**1. Install Xpra 3 build requirements from Red Hat distribution.**

For each RPM listed in Table 1, install the RPM and all dependencies if not already installed on the build host (see footnote [^1].  Examples:

    $ sudo yum install gtkglext-devel
    $ sudo yum install lcms2-devel
    $ sudo yum install libpciaccess-devel
    $ sudo yum install pulseaudio-utils
    $ sudo yum install python-netifaces
    $ sudo yum install python2-pkgconfig
    $ sudo yum install turbojpeg turbojpeg-devel

This list was compiled from a minimal RHEL 7 build host.  Most RHEL 7 build hosts will already have many of these RPMS.  Also, a few RPMs (see footnote [^2]) are only available from the [EPEL (Extra Packages for Enterprise Linux) repository](https://fedoraproject.org/wiki/EPEL].

Table 1: Xpra 3 Build Requirements
==TODO: Insert Table 1==
[^1]: Not usually installed on development servers/workstations
[^2]: Available from EPEL repository
[^3]: Xpra version is very similar to RHEL/EPEL version

