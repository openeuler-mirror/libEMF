Name:           libEMF
Version:        1.0.9
Release:        8
Summary:        A library for generating Enhanced Metafiles
License:        LGPLv2+ and GPLv2+
URL:            http://libemf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/libemf/libemf/%{version}/libemf-%{version}.tar.gz
Patch0000:      support-aarch64.patch

BuildRequires:  gcc-c++

%description
libEMF is designed to be used as a driver for other programs such as Grace and gunplot
to generate Enhanced Metafiles on systems which don't natively support the ECMA-234
Graphics Device Interface (GDI). It implements a limited subset of GDI.

%package        devel
Summary:        libEMF header files
Requires:       libEMF = %{version}-%{release} libstdc++-devel

%description    devel
Development header files for libEMF.

%package        help
Summary:        Documentation for libEMF

%description    help
Documentation for libEMF.

%prep
%autosetup -n libemf-%{version} -p1

%build
%configure --disable-static --enable-editing
%make_build

%install
export CPPROG="cp -p"
%make_install
%delete_la

%check
make check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog
%{_bindir}/printemf
%{_libdir}/libEMF.so.1*

%files          devel
%{_libdir}/libEMF.so
%{_includedir}/libEMF

%files          help
%doc doc/html/* NEWS README

%changelog
* Wed Jan 15 2020 qinjian <qinjian18@huawei.com> - 1.0.9-8
- rename patch

* Sat Dec 14 2019 lihao <lihao129@huawei.com> - 1.0.9-7
- Package Init

