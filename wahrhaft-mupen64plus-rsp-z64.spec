%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d
%define git_version 1374ffc147ad

Name:		wahrhaft-mupen64plus-rsp-z64
Version:	0.0.%{git_version}
Release:	2
Summary:	Low-level RSP processor plugin for the Mupen64Plus
Group:		Emulators
License:	GPLv2+
Url:		http://code.google.com/p/mupen64plus/
Source:         %{name}-%{git_version}.tar.bz2
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	mupen64plus-devel

%description
An experimental plugin for mupen64plus to replace the RSP plugin.


%prep
%setup -q -n %{name}-%{git_version}

%build
export CFLAGS="%{optflags}"
%make all -C projects/unix all COREDIR=%{_libdir}/ SHAREDIR=%{_datadir}/mupen64plus2/ PLUGINDIR=%{_libdir}/mupen64plus2/ V=1 

%install
make -C projects/unix install PREFIX="%{_prefix}" DESTDIR="%{buildroot}" SHAREDIR=%{_datadir}/mupen64plus2/ LIBDIR=%{_libdir}/mupen64plus2/ 

mv %{buildroot}%{_libdir}/mupen64plus2/mupen64plus/mupen64plus-rsp-z64.so %{buildroot}/%{_libdir}/mupen64plus2/
chmod -R 0755 %{buildroot}%{_libdir}

%files
%dir %{_libdir}/mupen64plus2
%{_libdir}/mupen64plus2/mupen64plus-rsp-z64.so

