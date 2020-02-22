Name:		nvenc
Version:	9.1.23
Release:	1%{?dist}
Summary:	An SDK for hardware accelerated video encode and decode on Windows and Linux.

Group:		Libraries/Graphics
License:	Nvidia
URL:		https://developer.nvidia.com/nvidia-video-codec-sdk
Source0:	Video_Codec_SDK_9.1.23.zip

BuildRequires:	ffmpeg-devel
BuildRequires:	libXdmcp-devel

%description
The SDK consists of two hardware acceleration interfaces: 

 - NVENCODE API for video encode acceleration
 - VDECODE API for video decode acceleration (formerly called NVCUVID API)

NVIDIA GPUs contain one or more hardware-based decoder and encoder(s)
(separate from the CUDA cores) which provides fully-accelerated
hardware-based video decoding and encoding for several popular codecs.
With decoding/encoding offloaded, the graphics engine and the CPU are
free for other operations.

License: https://developer.download.nvidia.com/designworks/DesignWorks_SDKs_Samples_Tools_License_distrib_use_rights_2017_06_13.pdf

%prep
%setup -q -n Video_Codec_SDK_%{version}


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Feb 13 2020 Eric Lemings <eric.lemings@ngc.com> - 9.1.23-1
- ground zero

