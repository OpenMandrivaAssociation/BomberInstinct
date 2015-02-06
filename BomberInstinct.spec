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


%changelog
* Mon Sep 12 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.9-13mdv2012.0
+ Revision: 699458
- rebuild

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.8.9-12mdv2011.0
+ Revision: 436868
- rebuild

* Sun Mar 29 2009 Michael Scherer <misc@mandriva.org> 0.8.9-11mdv2009.1
+ Revision: 362062
- add patch0, to fix bug 49246, by removing two level that do not exist

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8.9-10mdv2009.0
+ Revision: 243360
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.9-8mdv2008.1
+ Revision: 176496
- add missing file (bug #38229)

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.9-7mdv2008.0
+ Revision: 71595
- Import BomberInstinct



* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 0.8.9-7mdv2007.0
- xdg menu

* Thu Jun 15 2006 Lenny Cartier <lenny@mandriva.org> 0.8.9-6mdv2007.0
- rebuild

* Sun May 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.9-5mdk
- Rebuild
- use mkrel

* Fri May 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.9-4mdk
- Rebuild

* Tue May 11 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.9-3mdk
- fix menu section

* Wed Jun 25 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8.9-2mdk
- remove redundant buildrequires

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.9-1mdk
- add missing binary
- fix URL
- new version

* Tue Nov 12 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.8.8-4mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Removed obsolete Prefix tag
	- Move stuff to correct places
	- Cleanups

* Fri Aug 16 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.8-3mdk
- rebuild with new vorbis

* Mon Apr 29 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.8-2mdk
- rebuild with new alsa 

* Tue Feb 26 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.8-1mdk
- adapt package for Mandrake
