Name:		ffmpeg
Version:	4.2.2
Release:	1%{?dist}
Summary:	A complete, cross-platform solution to record, convert and stream audio and video.

Group:		Applications/Multimedia
License:	GPL
URL:		https://www.ffmpeg.org
Source0:	https://www.ffmpeg.org/releases/%{name}-%{version}.tar.xz

BuildRequires:	x264-devel
BuildRequires:	yasm

# See "Getting Started with FFmpeg/libav using NVIDIA GPUs" on web page
# <https://developer.nvidia.com/ffmpeg> for more details.
%if 0%{?with_cuda}
BuildRequires:	ffnvcodec
BuildRequires:	cuda
%endif

%description
FFmpeg is the leading multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play pretty much anything that
humans and machines have created.

%package devel
Summary:	Development environment for %{name} package
Group:		Development/libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
FFmpeg is the leading multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play pretty much anything that
humans and machines have created.


%prep
%setup -q


%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} \
%if 0%{?with_cuda}
--enable-cuda-nvcc --enable-cuvid --enable-nvenc --enable-nonfree --enable-libnpp \
--extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64 \
%endif
--enable-shared --disable-debug
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc COPYING* CREDITS README.md RELEASE_NOTES
%{_bindir}/*
%{_libdir}/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files devel
%doc MAINTAINERS doc/APIchanges
%defattr(-,root,root,-)
%dir %{_includedir}/*
%{_includedir}/*/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_docdir}/%{name}


%changelog
* Mon Feb 10 2020 Eric Lemings <eric.lemings@ngc.com> - 4.2.2-1
- initial version


