Summary:	Additional ghostscript fonts
Summary(pl):	Dodatkowe fonty dla interpretera ghostscript
Name:		ghostscript-fonts-other
Version:	5.50
Release:	1
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Copyright:	GPL
URL:		http://www.cs.wisc.edu/~ghost/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	ghostscript

%description
This package contains additional fonts for ghostscript.

Ghostscript is a PostScript interpretor. It can render both PostScript
and PDF compliant files to devices which include an X window, many printer
formats (including support for color printers), and popular graphics
file formats.

%description -l pl
Pakiet ten zawiera dodatkowe fonty dla interpretera ghostscript.

Ghostcript jest interpreterem PostScriptu, języku używanego do opisu formatu
dokumentu. Ghostscript potrafi przetworzyć dokument w formacie PostScript
i PDF %{name} szereg postaci wyjściowych: drukarki (włączając kolorowe), okno
X-Window i popularne formaty graficzne.

%prep
install -d fonts
cd fonts
gzip -dc %{SOURCE0} | tar xf -

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf fonts

%install
install -d $RPM_BUILD_ROOT/%{_datadir}/ghostscript/fonts
cp fonts/* $RPM_BUILD_ROOT/%{_datadir}/ghostscript/fonts

%files
%defattr(644,root,root,755)
%dir %{_datadir}/ghostscript/fonts
%attr(644,root,root) %{_datadir}/ghostscript/fonts/*
