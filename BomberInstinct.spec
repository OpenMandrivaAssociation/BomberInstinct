%define	name	BomberInstinct
%define version 0.8.9
%define release 14

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
Patch:		BomberInstinct-fix_missing_level.diff
URL:		http://bomberinstinct.sourceforge.net/index.html

BuildRequires:	pkgconfig(SDL_mixer) >= 1.2.0
# too much nested gcc
BuildRequires:	gcc-c++, gcc, gcc-cpp


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
export CC=gcc
export CXX=g++

%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
		
%make CXXFLAGS="-DNDEBUG %optflags"

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=BomberInstinct
Comment=Bomberman clone
Exec=%{_gamesbindir}/bi
Icon=BomberInstinct
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

cp data/Sprites/*.spr %{buildroot}%{_gamesdatadir}/BomberInstinct/Sprites

install -d -m755  %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
bzcat %{SOURCE1} > %{buildroot}%{_liconsdir}/%name.png
bzcat %{SOURCE2} > %{buildroot}%{_iconsdir}/%name.png
bzcat %{SOURCE3} > %{buildroot}%{_miconsdir}/%name.png


%files

%doc AUTHORS ChangeLog LISEZMOI LISEZMOI.Nived README README.Nived  
%doc docs/*.html docs/img scenario.txt 
%{_gamesbindir}/bi
%{_gamesbindir}/nived
%{_gamesbindir}/spred
%{_gamesdatadir}/BomberInstinct
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_liconsdir}/%name.png
%{_datadir}/applications/%{name}.desktop


