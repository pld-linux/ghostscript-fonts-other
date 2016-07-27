Summary:	Additional ghostscript fonts
Summary(pl.UTF-8):	Dodatkowe fonty dla interpretera ghostscript
Name:		ghostscript-fonts-other
Version:	6.0
Release:	7
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/fonts/gnu-gs-fonts-other-%{version}.tar.gz
# Source0-md5:	33457d3f37de7ef03d2eea05a9e6aa4f
Source1:	%{name}.Fontmap
Source2:	%{name}.fonts.scale
URL:		http://www.cs.wisc.edu/~ghost/
BuildRequires:	t1utils
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm
%define		_t1pfmdir	%{_t1fontsdir}/pfm

%description
This package contains additional fonts for ghostscript.

Ghostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l pl.UTF-8
Pakiet ten zawiera dodatkowe fonty dla interpretera ghostscript.

Ghostcript jest interpreterem PostScriptu, języku używanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyć dokument w formacie
PostScript i PDF na szereg postaci wyjściowych: drukarki (włączając
kolorowe), okno X-Window i popularne formaty graficzne.

%prep
%setup -q -n fonts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_t1fontsdir},%{_t1afmdir},%{_t1pfmdir}}

# present in t1lib-fonts
rm -f bch*

install *.gsf $RPM_BUILD_ROOT%{_t1fontsdir}
install *.afm $RPM_BUILD_ROOT%{_t1afmdir}
install *.pfm $RPM_BUILD_ROOT%{_t1pfmdir}

for f in *.pfa ; do
	t1binary $f $RPM_BUILD_ROOT%{_t1fontsdir}/`basename $f .pfa`.pfb
done

install %{SOURCE1} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%{_t1fontsdir}/Fontmap.%{name}
%{_t1fontsdir}/fonts.scale.%{name}
%{_t1fontsdir}/fcyr*.gsf
%{_t1fontsdir}/fhirw.gsf
%{_t1fontsdir}/fkarw.gsf
%{_t1fontsdir}/hrger*.gsf
%{_t1fontsdir}/hrgk*.gsf
%{_t1fontsdir}/hrgrr*.gsf
%{_t1fontsdir}/hritr*.gsf
%{_t1fontsdir}/hrpl*.gsf
%{_t1fontsdir}/hrsc*.gsf
%{_t1fontsdir}/hrsyr.gsf
%{_t1fontsdir}/u003043t.gsf
%{_t1fontsdir}/u004006t.gsf
%{_t1fontsdir}/hrger.pfb
%{_t1fontsdir}/hrgrr.pfb
%{_t1fontsdir}/hritr.pfb
%{_t1fontsdir}/hrpld*.pfb
%{_t1fontsdir}/hrplt*.pfb
%{_t1fontsdir}/hrsc*.pfb
%{_t1fontsdir}/put*.pfb
%{_t1afmdir}/fcyr*.afm
%{_t1afmdir}/u003043t.afm
%{_t1afmdir}/u004006t.afm
%{_t1pfmdir}/fhirw.pfm
%{_t1pfmdir}/fkarw.pfm
%{_t1pfmdir}/u003043t.pfm
%{_t1pfmdir}/u004006t.pfm
