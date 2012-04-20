%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d
%define git_version 1374ffc147ad

Name:           wahrhaft-mupen64plus-rsp-z64
Version:        0.0.%{git_version}
Release:        %mkrel 1
Summary:        Arachnoid Plugin for mupen64plus
Group:          Emulators
License:        GPLv2+
Url:            http://code.google.com/p/mupen64plus/
AutoReqProv:    on
BuildRequires:  gcc-c++ libSDL-devel libpng-devel libsamplerate-devel 
BuildRequires:  freetype2-devel zlib-devel lirc-devel
Source:         %{name}-%{git_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An experimental plugin for mupen64plus to replace the RSP plugin.


%prep
%setup -q -n %{name}-%{git_version}

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} all -C projects/unix all COREDIR=%{_libdir}/ SHAREDIR=%{_datadir}/mupen64plus2/ PLUGINDIR=%{_libdir}/mupen64plus2/ V=1 

%install
make -C projects/unix install PREFIX="%{_prefix}" DESTDIR="%{buildroot}" SHAREDIR=%{_datadir}/mupen64plus2/ LIBDIR=%{_libdir}/mupen64plus2/ 

mv %{buildroot}/%{_libdir}/mupen64plus2/mupen64plus/mupen64plus-rsp-z64.so %{buildroot}/%{_libdir}/mupen64plus2/
chmod -R 0755 %{buildroot}%{_libdir}


%post

%postun

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_libdir}/mupen64plus2
%{_libdir}/mupen64plus2/mupen64plus-video-rsp-z64.so

