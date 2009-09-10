%define	name	BomberInstinct
%define version 0.8.9
%define release %mkrel 12

Summary:	Kill the other players with bombs that throw flames
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png.bz2
Source2:	%{name}-32.png.bz2
Source3:	%{name}-16.png.bz2
Patch:      BomberInstinct-fix_missing_level.diff
URL:		http://bomberinstinct.sourceforge.net/index.html
BuildRoot:	%_tmppath/%{name}-%{version}-%{release}-root
BuildRequires:	libSDL_mixer-devel >= 1.2.0

%description
BomberInstinct is part like Bomberman, because you must kill
the other players with bombs that throw flames vertically and
horizontally, but it's much more strategical because you have to
do with the elements of a maze (arrows, tunnels, teleportations,
and many more...), and with the special powers of each character.
(multiplayer on one computer only)

%prep
%setup -q
%patch -p0

%build
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
		
%make CXXFLAGS="-DNDEBUG %optflags"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=BomberInstinct
Comment=Bomberman clone
Exec=%_gamesbindir/bi
Icon=BomberInstinct
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

#gw missing file(s):
cp data/Sprites/*.spr %buildroot%{_gamesdatadir}/BomberInstinct/Sprites

mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%_miconsdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_liconsdir}/%name.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_iconsdir}/%name.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_miconsdir}/%name.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog LISEZMOI LISEZMOI.Nived README README.Nived  
%doc docs/*.html docs/img scenario.txt 
%{_gamesbindir}/bi
%{_gamesbindir}/nived
%{_gamesbindir}/spred
%{_gamesdatadir}/BomberInstinct
%{_iconsdir}/%name.png
%{_iconsdir}/mini/%name.png
%{_liconsdir}/%name.png
%_datadir/applications/mandriva*
