Name:		xditview
Version:	1.0.2
Release:	%mkrel 2
Summary:	Display ditroff output
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
Display ditroff output.

%prep
%setup -q -n %{name}-%{version}

%build
#autoreconf -ifs
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%defattr(-,root,root)
%{_bindir}/xditview
%{_datadir}/X11/app-defaults/Xditview
%{_datadir}/X11/app-defaults/Xditview-chrtr
%{_includedir}/X11/bitmaps/ldblarrow
%{_includedir}/X11/bitmaps/rdblarrow
%{_mandir}/man1/xditview.1*
