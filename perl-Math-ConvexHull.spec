#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	ConvexHull
%include	/usr/lib/rpm/macros.perl
Summary:	Math::ConvexHull - Calculate convex hulls using Graham's scan (n*log(n))
Name:		perl-Math-ConvexHull
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d9225c5fadf5c71172cd88c81661d4d
URL:		http://search.cpan.org/dist/Math-ConvexHull/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::ConvexHull is a simple module that calculates convex hulls from a set
of points in 2D space. It is a straightforward implementation of the algorithm
known as Graham's scan which, with complexity of O(n*log(n)), is the fastest
known method of finding the convex hull of an arbitrary set of points.
There are some methods of eliminating points that cannot be part of the
convex hull. These may or may not be implemented in a future version.

The implementation cannot deal with duplicate points. Therefore, points
which are very, very close (think floating point close) to the
previous point are dropped since version 1.02 of the module.
However, if you pass in randomly ordered data which contains duplicate points,
this safety measure might not help you. In that case, you will have to
remove duplicates yourself.

None by default, but you may choose to have the convex_hull() subroutine
exported to your namespace using standard Exporter semantics.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/*.pm
%{_mandir}/man3/*
