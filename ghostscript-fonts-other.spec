Summary:	Additional ghostscript fonts
Summary(pl):	Dodatkowe fonty dla interpretera ghostscript
Name:		ghostscript-fonts-other
Version:	5.50
Release:	3
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
License:	GPL
URL:		http://www.cs.wisc.edu/~ghost/
Source0:	%{name}-%{version}.tar.gz
Requires:	ghostscript
Prereq:		/usr/bin/type1inst
Requires:	type1inst >= 0.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains additional fonts for ghostscript.

Ghostscript is a PostScript interpretor. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l pl
Pakiet ten zawiera dodatkowe fonty dla interpretera ghostscript.

Ghostcript jest interpreterem PostScriptu, jêzyku u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF %{name} szereg postaci wyj¶ciowych: drukarki
(w³±czaj±c kolorowe), okno X-Window i popularne formaty graficzne.

%prep
install -d fonts
cd fonts
gzip -dc %{SOURCE0} | tar xf -

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf fonts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/fonts/Type1
cp fonts/* $RPM_BUILD_ROOT/%{_datadir}/fonts/Type1

%post
cd %{_datadir}/fonts/Type1
/usr/bin/type1inst -nolog

%postun
cd %{_datadir}/fonts/Type1
/usr/bin/type1inst -nolog

%files
%defattr(644,root,root,755)
%attr(644,root,root) %{_datadir}/fonts/Type1/*
