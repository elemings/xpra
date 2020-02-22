Name:		libwebp1
Version:	1.0.3
Release:	1%{?dist}
Summary:	A new image format for the Web

Group:		Applications/Multimedia
License:	BSD
URL:		https://developers.google.com/speed/webp
Source0:	libwebp-%{version}.tar.gz

%description
WebP is a modern image format that provides superior lossless and lossy
compression for images on the web. Using WebP, webmasters and web
developers can create smaller, richer images that make the web faster.

%package tools
Summary:	Development tools for the %{name} package
Group:		Development/Tools
Requires:	%{name} = %{version}

%description tools
WebP is a modern image format that provides superior lossless and lossy
compression for images on the web. Using WebP, webmasters and web
developers can create smaller, richer images that make the web faster.

%package devel
Summary:	Development environment for the %{name} package
Group:		Development/libraries
Requires:	%{name} = %{version}
Requires:	pkgconfig

%description devel
WebP is a modern image format that provides superior lossless and lossy
compression for images on the web. Using WebP, webmasters and web
developers can create smaller, richer images that make the web faster.


%prep
%setup -q -n libwebp-%{version}


%build
%configure \
	--enable-shared \
	--enable-static \
	--enable-libwebpdecoder \
	--enable-libwebpmux \
	--enable-libwebpdemux
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS COPYING NEWS PATENTS README
%{_libdir}/*.so.*

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%dir %{_includedir}/webp
%{_includedir}/webp/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Tue Feb  4 2020 Eric Lemings <eric.lemings@ngc.com> - 1.0.3-1
- initial version

