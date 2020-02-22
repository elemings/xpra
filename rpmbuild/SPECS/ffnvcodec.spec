Name:		ffnvcodec
Version:	9.1.23.2
Release:	1%{?dist}
Summary:	FFmpeg version of Nvidia Codec SDK headers

Group:		Development/Libraries
License:	GPL
URL:		https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
This package contains the header files required to build Nvidia-related
components of the ffmpeg package.

%prep
%setup -q


%install
make install PREFIX=%{_prefix} LIBDIR=share DESTDIR=%{buildroot}


%files
%dir %{_includedir}/ffnvcodec
%{_includedir}/ffnvcodec/*.h
%{_datadir}/pkgconfig/ffnvcodec.pc
%doc README

%changelog
* Thu Jan 23 2020 Eric Lemings <eric.lemings@ngc.com> - 9.1.23.2-1
- initial version

