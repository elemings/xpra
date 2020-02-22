
Name:		libyuv
Version:	0.0.1744
Release:	1%{?dist}
Summary:	YUV scaling and conversion functionality

Group:		Applications/Multimedia
License:	BSD
URL:		https://chromium.googlesource.com/libyuv/libyuv
Source0:	%{name}-%{version}.tar.xz
Patch1:		libyuv-0001-Use-a-proper-so-version.patch
Patch2:		libyuv-0002-Link-against-shared-library.patch
Patch3:		libyuv-0003-Disable-static-library.patch
Patch4:		libyuv-0004-Don-t-install-conversion-tool.patch
Patch5:		libyuv-0005-Use-library-suffix-during-installation.patch
Patch6:		libyuv-0006-Link-main-library-against-libjpeg.patch

BuildRequires:	libjpeg-turbo-devel

%description
libyuv is an open source project that includes YUV scaling and conversion functionality.

  - Scale YUV to prepare content for compression, with point, bilinear or box filter.
  - Convert to YUV from webcam formats for compression.
  - Convert to RGB formats for rendering/effects.
  - Rotate by 90/180/270 degrees to adjust for mobile devices in portrait mode.
  - Optimized for SSSE3/AVX2 on x86/x64.
  - Optimized for Neon on Arm.
  - Optimized for MSA on Mips.

%package devel
Summary:	Development environment for %{name} package
Group:		Development/libraries
Requires:	%{name} = %{version}

%description devel
libyuv is an open source project that includes YUV scaling and conversion functionality.

  - Scale YUV to prepare content for compression, with point, bilinear or box filter.
  - Convert to YUV from webcam formats for compression.
  - Convert to RGB formats for rendering/effects.
  - Rotate by 90/180/270 degrees to adjust for mobile devices in portrait mode.
  - Optimized for SSSE3/AVX2 on x86/x64.
  - Optimized for Neon on Arm.
  - Optimized for MSA on Mips.


%prep
%autosetup


%global optflags -std=c++11 %{optflags}

%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS LICENSE PATENTS README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/libyuv.h
%dir %{_includedir}/libyuv
%{_includedir}/libyuv/*
%{_includedir}/libyuv.h
%{_libdir}/*.so


%changelog
* Fri Feb  7 2020 Eric Lemings <eric.lemings@ngc.com> - 0.0.1744-1
- initial version

