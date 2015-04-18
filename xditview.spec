Name:		xditview
Version:	1.0.4
Release:	1
Summary:	Display ditroff output
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: xaw-devel >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1

%description
Display ditroff output.

%prep
%setup -q

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xditview
%{_datadir}/X11/app-defaults/Xditview
%{_datadir}/X11/app-defaults/Xditview-chrtr
%{_includedir}/X11/bitmaps/ldblarrow
%{_includedir}/X11/bitmaps/rdblarrow
%{_mandir}/man1/xditview.1*
