
# x264 version numbers consist of total revision count followed by
# first 7 characters of the most recent Git commit hash.  These are
# seperated by a dash but this is not allowed in RPM Version macros
# so the usual dot separator is used instead.

%define	revision r2991
%define commit 1771b55

Name:		x264
Version:	%{revision}.%{commit}
Release:	1%{?dist}
Summary:	Video stream codec for H.264/MPEG-4 AVC

Group:		Applications/Multimedia
License:	GPL
URL:		http://www.videolan.org/developers/x264.html
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	nasm

%description
x264 is a free software library and application for encoding video
streams into the H.264/MPEG-4 AVC compression format, and is released
under the terms of the GNU GPL.

%package devel
Summary:	Development environment for the %{name} package
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	pkgconfig

%description devel
x264 is a free software library and application for encoding video
streams into the H.264/MPEG-4 AVC compression format, and is released
under the terms of the GNU GPL.

%prep
%setup -q


%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-shared --enable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
%{_bindir}/x264
%{_libdir}/libx264.so.159
%{_libdir}/pkgconfig/%{name}.pc

%files devel
%{_includedir}/x264.h
%{_includedir}/x264_config.h
%{_libdir}/libx264.a
%{_libdir}/libx264.so


%changelog
* Thu Feb  6 2020 Eric Lemings <eric.lemings@ngc.com> - r2991.1771b55-1
- initial version

