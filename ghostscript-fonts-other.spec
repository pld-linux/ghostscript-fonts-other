Summary:	Additional ghostscript fonts
Summary(pl):	Dodatkowe fonty dla interpretera ghostscript
Name:		ghostscript-fonts-other
Version:	6.0
Release:	3
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.cs.wisc.edu/ghost/gnu/fonts/gnu-gs-fonts-other-%{version}.tar.gz
# Source0-md5:	33457d3f37de7ef03d2eea05a9e6aa4f
Source1:	%{name}.Fontmap
Source2:	%{name}.fonts.scale
URL:		http://www.cs.wisc.edu/~ghost/
BuildRequires:	t1utils
Requires(post,postun):	fontpostinst
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

%description -l pl
Pakiet ten zawiera dodatkowe fonty dla interpretera ghostscript.

Ghostcript jest interpreterem PostScriptu, jêzyku u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF na szereg postaci wyj¶ciowych: drukarki (w³±czaj±c
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
%{_t1fontsdir}/*.gsf
%{_t1fontsdir}/*.pfb
%{_t1afmdir}/*.afm
%{_t1pfmdir}/*.pfm
%{_t1fontsdir}/*.%{name}
