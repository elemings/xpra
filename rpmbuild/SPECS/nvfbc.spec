Name:		nvfbc
Version:	7.1.6
Release:	1%{?dist}
Summary:	Enables developers to capture and encode display content.

Group:		Libraries/Graphics
License:	Nvidia
URL:		https://developer.nvidia.com/capture-sdk
# note: original distribution contains extra subdirectory level
Source0:	Capture_Linux_v%{version}.zip

%if 0%{?with_cuda}
BuildRequires:	http://glew.sourceforge.net
%endif

%description
The NVIDIA Capture SDK enables remote desktop displays on NVIDIA hardware
(local, remote or cloud). It provides the ability to capture the desktop
buffer as an image or steam of images that can be compressed as a video
bitstream for transmission to remote clients or for storing locally.

License: https://developer.nvidia.com/capture-sdk-software-license-agreement

%prep
%setup -q -n Capture_Linux_v%{version}


%build
cd NvFBC/samples
make %{?_smp_mflags}


%install
#make install DESTDIR=%{buildroot}
( cd NvFBC/inc
install -d %{buildroot}%{_includedir}/%{name}
install -p *.h %{buildroot}%{_includedir}/%{name} )
( cd NvFBC/samples/inc
install -p *.h %{buildroot}%{_includedir}/%{name} )
( cd NvFBC/samples
install -d %{buildroot}%{_datadir}/%{name}
cp -rp Nv* common makefile %{buildroot}%{_datadir}/%{name} )


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

