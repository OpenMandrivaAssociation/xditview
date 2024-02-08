Name:		xditview
Version:	1.0.7
Release:	1
Summary:	Display ditroff output
Group:		Development/X11
Url:		https://gitlab.freedesktop.org/xorg/app/xditview
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(xt) >= 1.0.0
BuildRequires:	xaw-devel >= 1.0.1
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1

%description
Display ditroff output.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xditview
%{_datadir}/X11/app-defaults/Xditview
%{_datadir}/X11/app-defaults/Xditview-chrtr
%{_includedir}/X11/bitmaps/ldblarrow
%{_includedir}/X11/bitmaps/rdblarrow
%doc %{_mandir}/man1/xditview.1*
