Name:       corrade
Version:    2020.06
Release:    1
Summary:    C++11/C++14 multiplatform utility library
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake, git, gcc-c++

%description
Provides debugging, portability, configuration, resource management and
filesystem utilites and plugin management with dependency handling.

%package devel
Summary: Corrade development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for developing with Corrade.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_TESTS=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_libdir}/*.so*
strip $RPM_BUILD_ROOT/%{_bindir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
#%doc COPYING COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_bindir}/corrade-rc
%{_includedir}/Corrade
%{_datadir}/cmake/Corrade

#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
