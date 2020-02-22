Name:		ffmpeg
Version:	4.2.2
Release:	1%{?dist}
Summary:	A complete, cross-platform solution to record, convert and stream audio and video.

Group:		Applications/Multimedia
License:	GPL
URL:		http://www.ffmpeg.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires:	x264-devel
BuildRequires:	yasm

# See "Getting Started with FFmpeg/libav using NVIDIA GPUs" on web page
# <https://developer.nvidia.com/ffmpeg> for more details.
%if 0%{?with_nvidia}
BuildRequires:	ffnvcodec
BuildRequires:	cuda
%endif

%description
FFmpeg is the leading multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play pretty much anything that
humans and machines have created.


%prep
%setup -q


%build
%if 0%{?with_nvidia}
%configure --enable-cuda-sdk --enable-cuvid --enable-nvenc --enable-nonfree --enable-libnpp \
--extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64
%else
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

