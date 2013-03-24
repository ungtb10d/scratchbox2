Summary: 	Scratchbox2 crosscompiling environment
License: 	LGPL
Name: 		scratchbox2
Version: 	2.3.90
Release: 	3
Source: 	%{name}-%{version}.tar.gz
Prefix: 	/usr
Group: 		Development/Tools
Patch0:		scratchbox2-2.3.27-usrsrc.patch
Patch1:		scratchbox2-2.3.52-wrapperargs.patch
Patch2:		0001-accel-localedef.patch
Patch3:		0002-support-ccache.patch
Patch4:		0003-accel-ccache.patch
Patch5:		0004-accel-qtchooser-qmake.patch
ExclusiveArch:	%{ix86}
BuildRequires:	make
Requires:	fakeroot

%description
Scratchbox2 crosscompiling environment

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
./autogen.sh
./configure
make

%install
make install prefix=$RPM_BUILD_ROOT/usr

%files
%defattr(-,root,root)
/usr/bin/sb2*
/usr/lib/libsb2/*
%ifarch x86_64
/usr/lib32/libsb2/*
%endif
/usr/share/scratchbox2/*

%doc %attr(0444,root,root) /usr/share/man/man1/*
%doc %attr(0444,root,root) /usr/share/man/man7/*
