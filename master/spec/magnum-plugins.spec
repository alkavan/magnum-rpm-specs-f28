Name:       magnum-plugins
Version:    master
Release:    1
Summary:    Plugins for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, DevIL, libpng, libjpeg-turbo, freetype, assimp, faad2-libs, glslang, spirv-tools-libs
BuildRequires: cmake, git, gcc-c++, DevIL-devel, libpng-devel, libjpeg-turbo-devel, freetype-devel, assimp-devel, faad2-devel, harfbuzz-devel, glslang-devel, spirv-tools-devel
Source1: https://github.com/BinomialLLC/basis_universal/archive/2f43afcc97d0a5dafdb73b4e24e123cf9687a418.zip
Source2: https://github.com/zeux/meshoptimizer/archive/v0.15.zip

%description
Here are various plugins for the Magnum C++11/C++14 graphics engine -
asset import and conversion, text rendering and more.

%package devel
Summary: MagnumPlugins development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for the Magnum plugins collection.

%prep
%setup -c -n %{name}-%{version}

%build
unzip %{SOURCE1} -d %{_builddir}/
unzip %{SOURCE2} -d %{_builddir}/

mv %{_builddir}/meshoptimizer-0.15 %{name}-%{version}/src/external/meshoptimizer

mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DBASIS_UNIVERSAL_DIR=%{_builddir}/basis_universal-2f43afcc97d0a5dafdb73b4e24e123cf9687a418 \
  -DBUILD_TESTS=ON \
  -DBUILD_GL_TESTS=ON \
  -DWITH_ASSIMPIMPORTER=ON \
  -DWITH_BASISIMAGECONVERTER=ON \
  -DWITH_BASISIMPORTER=ON \
  -DWITH_DDSIMPORTER=ON \
  -DWITH_DEVILIMAGEIMPORTER=ON \
  -DWITH_DRFLACAUDIOIMPORTER=ON \
  -DWITH_DRMP3AUDIOIMPORTER=ON \
  -DWITH_DRWAVAUDIOIMPORTER=ON \
  -DWITH_FAAD2AUDIOIMPORTER=ON \
  -DWITH_FREETYPEFONT=ON \
  -DWITH_GLSLANGSHADERCONVERTER=ON \
  -DWITH_HARFBUZZFONT=ON \
  -DWITH_ICOIMPORTER=ON \
  -DWITH_JPEGIMAGECONVERTER=ON \
  -DWITH_JPEGIMPORTER=ON \
  -DWITH_MESHOPTIMIZERSCENECONVERTER=ON \
  -DWITH_MINIEXRIMAGECONVERTER=ON \
  -DWITH_OPENGEXIMPORTER=ON \
  -DWITH_PNGIMAGECONVERTER=ON \
  -DWITH_PNGIMPORTER=ON \
  -DWITH_PRIMITIVEIMPORTER=ON \
  -DWITH_SPIRVTOOLSSHADERCONVERTER=ON \
  -DWITH_STANFORDIMPORTER=ON \
  -DWITH_STANFORDSCENECONVERTER=ON \
  -DWITH_STBIMAGECONVERTER=ON \
  -DWITH_STBIMAGEIMPORTER=ON \
  -DWITH_STBTRUETYPEFONT=ON \
  -DWITH_STBVORBISAUDIOIMPORTER=ON \
  -DWITH_STLIMPORTER=ON \
  -DWITH_TINYGLTFIMPORTER=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_libdir}/*.so*
strip $RPM_BUILD_ROOT/%{_libdir}/magnum-d/*/*.so*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/basis_universal-2f43afcc97d0a5dafdb73b4e24e123cf9687a418

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_libdir}/magnum-d/*/*

#%doc COPYING

%files devel
%defattr(-,root,root,-)
%{_includedir}/Magnum
%{_includedir}/MagnumPlugins
%{_includedir}/MagnumExternal
%{_datadir}/cmake/MagnumPlugins

%changelog
# TODO: changelog
