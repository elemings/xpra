Name:           nvenc
Version:        9.1.23
Release:        1%{?dist}
Summary:        A comprehensive set of APIs for hardware accelerated video encode and decode

Group:          Libraries/Graphics
#License:        https://developer.nvidia.com/nvidia-video-codec-sdk-license-agreement # previous license?
License:        https://developer.nvidia.com/designworks/sdk-samples-tools-software-license-agreement
URL:            https://developer.nvidia.com/nvidia-video-codec-sdk
Source0:        Video_Codec_SDK_%{version}.zip

BuildRequires:  ffmpeg-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  vulkan-devel
# Required for:
# - libnvcuvid.so (NVDECODE)
# - libnvidia-encode.so (NVENCODE)
Requires:       nvidia-driver-devel >= 2:396.24

%description
The SDK consists of two hardware acceleration interfaces: 

 * NVENCODE API for video encode acceleration
 * NVDECODE API for video decode acceleration (formerly called NVCUVID API)

NVIDIA GPUs contain one or more hardware-based decoder and encoder(s) (separate
from the CUDA cores) which provides fully-accelerated hardware-based video
decoding and encoding for several popular codecs. With decoding/encoding
offloaded, the graphics engine and the CPU are free for other operations.

GPU hardware accelerator engine for video decoding (referred to as NVDEC)
supports faster than real-time decoding which makes it suitable to be used
for transcoding applications, in addition to video playback applications.

%prep
%setup -q -n Video_Codec_SDK_%{version}


%build
cd Samples
make %{?_smp_mflags}


%install
#make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_includedir}/%{name}
install -p include/* %{buildroot}%{_includedir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
install -p -m755 \
Samples/AppDecode/AppDec/AppDec \
Samples/AppDecode/AppDecGL/AppDecGL \
Samples/AppDecode/AppDecImageProvider/AppDecImageProvider \
Samples/AppDecode/AppDecLowLatency/AppDecLowLatency \
Samples/AppDecode/AppDecMem/AppDecMem \
Samples/AppDecode/AppDecMultiFiles/AppDecMultiFiles \
Samples/AppDecode/AppDecMultiInput/AppDecMultiInput \
Samples/AppDecode/AppDecPerf/AppDecPerf \
Samples/AppEncode/AppEncCuda/AppEncCuda \
Samples/AppEncode/AppEncDec/AppEncDec \
Samples/AppEncode/AppEncGL/AppEncGL \
Samples/AppEncode/AppEncLowLatency/AppEncLowLatency \
Samples/AppEncode/AppEncME/AppEncME \
Samples/AppEncode/AppEncPerf/AppEncPerf \
Samples/AppEncode/AppEncQual/AppEncQual \
Samples/AppEncode/AppMotionEstimationVkCuda/AppMotionEstimationVkCuda \
Samples/AppTranscode/AppTrans/AppTrans \
Samples/AppTranscode/AppTransOneToN/AppTransOneToN \
Samples/AppTranscode/AppTransPerf/AppTransPerf \
%{buildroot}%{_datadir}/%{name}
cp -rp Samples/NvCodec %{buildroot}%{_datadir}/%{name}


install -d %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: %{name}
Description: Nvidia Video Codec SDK
Version: %{version}

Cflags: -I\${includedir}
Libs: -L%{_libdir} -lnvidia-encode
EOF


%files
%doc LicenseAgreement.pdf NOTICES.txt ReadMe.txt Release_notes.txt deprecation_notices.txt
%doc doc/*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*


%changelog
* Thu Feb 13 2020 Eric Lemings <eric.lemings@ngc.com> - 9.1.23-1
- ground zero

