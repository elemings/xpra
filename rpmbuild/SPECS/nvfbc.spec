Name:           nvfbc
Version:        7.1.6
Release:        1%{?dist}
Summary:        Enables developers to capture and encode display content.

Group:          Libraries/Graphics
License:        https://developer.nvidia.com/capture-sdk-software-license-agreement
URL:            https://developer.nvidia.com/capture-sdk
# note: original distribution contains extra subdirectory level
Source0:        Capture_Linux_v%{version}.zip

BuildRequires:  glew
# Required for:
# - libnvidia-fbc.so
Requires:       nvidia-driver-NvFBCOpenGL >= 2:396.24

%description
The NVIDIA Capture SDK enables remote desktop displays on NVIDIA hardware
(local, remote or cloud). It provides the ability to capture the desktop
buffer as an image or steam of images that can be compressed as a video
bitstream for transmission to remote clients or for storing locally.

%prep
%setup -q -n Capture_Linux_v%{version}


%build
cd NvFBC/samples
make %{?_smp_mflags}


%install
#make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_includedir}/%{name}
install -p NvFBC/inc/*.h %{buildroot}%{_includedir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
install -p NvFBC/samples/inc/*.h %{buildroot}%{_datadir}/%{name}
install -p -m755 \
NvFBC/samples/NvFBCCUDAAsync/NvFBCCUDAAsync \
NvFBC/samples/NvFBCHwEnc/NvFBCHwEnc \
NvFBC/samples/NvFBCHwEncCaps/NvFBCHwEncCaps \
NvFBC/samples/NvFBCMultiThread/NvFBCMultiThread \
NvFBC/samples/NvFBCSharedContext/NvFBCSharedContext \
NvFBC/samples/NvFBCToGL/NvFBCToGL \
NvFBC/samples/NvFBCToGLEnc/NvFBCToGLEnc \
%{buildroot}%{_datadir}/%{name}

install -d %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: %{name}
Description: Nvidia Capture SDK
Version: %{version}

Cflags: -I\${includedir}
Libs: -L%{_libdir} -lnvidia-fbc -lnvidia-ifr
EOF


%files
%doc Changelog LICENSE README ReleaseNotes.txt
%doc NvFBC/docs/*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%doc docs/*


%changelog
* Thu Feb 13 2020 Eric Lemings <eric.lemings@ngc.com> - 7.1.6-1
- ground zero

