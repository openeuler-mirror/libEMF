Name:           libEMF
Version:        1.0.13
Release:        2
Summary:        A library for generating Enhanced Metafiles
License:        LGPLv2+ and GPLv2+
URL:            http://libemf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/libemf/libemf/%{version}/libemf-%{version}.tar.gz
%ifarch loongarch64
Patch0:         0001-libEMF-add-loongarch64.patch
%endif

BuildRequires:  gcc-c++ chrpath

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
chrpath -d %{buildroot}%{_bindir}/printemf
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
* Thu Jul 20 2023 doupengda <doupengda@loongson.cn> - 1.0.13-2
- libEMF add support for loongarch64

* Tue Sep 28 2021 yaoxin <yaoxin30@huawei.com> - 1.0.13-1
- Upgrade libEMF to 1.0.13; fix CVE-2020-13999 CVE-2020-11863 CVE-2020-11865 CVE-2020-11866 CVE-2020-11864

* Fri Sep 10 2021 Pengju Jiang <jiangpengju2@huawei.com> - 1.0.9-9
- solve the rpath problem

* Wed Jan 15 2020 qinjian <qinjian18@huawei.com> - 1.0.9-8
- rename patch

* Sat Dec 14 2019 lihao <lihao129@huawei.com> - 1.0.9-7
- Package Init

