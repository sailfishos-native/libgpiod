%define libgpiod_soversion 2
%define libgpiodcxx_soversion 1
%define libgpiomockup_soversion 0
Name:           libgpiod
Version:        1.6.3
Release:        0
Summary:        C library and tools for interacting with the linux GPIO character device
License:        LGPL-2.1-or-later
URL:            https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:        https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kmod-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  kernel-headers

%description
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

%package utils
Summary:        Tools for interacting with the linux GPIO character device
Provides:       libgpiod = %{version}-%{release}
Obsoletes:      libgpiod < %{version}-%{release}

%description utils
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Command-line tools part.

%package -n libgpiod%{libgpiod_soversion}
Summary:        C library for interacting with the linux GPIO character device
Conflicts:      libgpiod1

%description -n libgpiod%{libgpiod_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C library part.

%package -n libgpiodcxx%{libgpiodcxx_soversion}
Summary:        C++library for interacting with the linux GPIO character device
Conflicts:      libgpiod1

%description -n libgpiodcxx%{libgpiodcxx_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C++ library part.

%package -n libgpiomockup%{libgpiomockup_soversion}
Summary:        C library for interacting with the linux GPIO character device
Conflicts:      libgpiod1

%description -n libgpiomockup%{libgpiomockup_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

GPIO mockup library part.

%package devel
Summary:        Devel files for libgpiod
Requires:       %{name} = %{version}
Requires:       libgpiod%{libgpiod_soversion} = %{version}
Requires:       libgpiodcxx%{libgpiodcxx_soversion} = %{version}

%description devel
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Devel files part.

%package -n python3-gpiod
Summary:        Python binding for libgpiod
Provides:       python-libgpiod
Obsoletes:      python-libgpiod

%description -n python3-gpiod
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Python binding part.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
./autogen.sh \
	--enable-tools=yes \
	--enable-bindings-python \
	--enable-bindings-cxx \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.{a,la}
rm -rf %{buildroot}%{python3_sitearch}/*.{a,la}

%post -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%postun -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%post -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig
%postun -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig

%files utils
%{_bindir}/gpio*

%files -n libgpiod%{libgpiod_soversion}
%{_libdir}/libgpiod.so.*

%files -n libgpiodcxx%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.*

%files devel
%{_includedir}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgpiod.pc
%{_libdir}/pkgconfig/libgpiodcxx.pc

%files -n python3-gpiod
%{python3_sitearch}/*.so

%changelog

