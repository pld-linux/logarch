%include	/usr/lib/rpm/macros.perl
Summary:	Rotates, compresses, removes and mails system log files
Summary(de):	Rotiert, komprimiert und verschickt Systemlogs
Summary(es):	Hace el rutado, comprime y envía mail de logs del sistema
Summary(fr):	Fait tourner, compresse, et envoie par mail les connexions au système
Summary(pl):	System rotacji i kompresowania logów
Summary(tr):	Sistem günlüklerini yönlendirir, sýkýþtýrýr ve mektup olarak yollar
Name:		logarch
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/System
#Source0:	http://www.lohmueller.ch/projects/logarch/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	9e5fb7dff09fff3454a9f79014b38668
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The logarch utility is designed to simplify the administration of log
files on a system which generates a lot of log files. Logarch allows
for the automatic rotation compression, removal and mailing of log
files. Logarch can be set to handle a log file daily, weekly, monthly
or when the log file gets to a certain size. Normally, logarch runs as
a daily cron job.

%description -l de
Logarch vereinfacht die Verwaltung von Systemen, die sehr viele
Log-Dateien erzeugen, indem es das automatische Rotieren,
Komprimieren, Entfernen, und Senden von Log-Dateien ermöglicht. Jede
Log-Datei kann täglich, wöchentlich oder monatlich verarbeitet werden,
wenn sie zu groß wird.

%description -l es
Logarch fue proyectado para facilitar la administración de sistemas
que generan gran número de archivos de log. Permite automatización en
la rotación, compresión, remoción y envío de mail de archivos de logs.
Cada archivo de log puede ser tratado diariamente, semanalmente,
mensualmente o cuanto crezca demasiado.

%description -l fr
Logarch est conçu pour faciliter l'administration de systèmes qui
générent un grand nombre de fichiers de \"log\". Il permet le
roulement, la suppréssion la compression et l'envoi automatiques de
ces fichiers. Chaque fichier de \"log\" peut être pris en charge de
manière quotidienne, hebdomadaire, mensuelle, ou quand il devient trop
volumineux.

%description -l pl
Logarch jest przeznaczony do ³atwej administracji plikami logów.
Program ten pozwala na automatyczn± kompresjê logów. Mo¿e kontrolowaæ
logi raz dziennie, raz na miesi±c, raz na tydzieñ lub wtedy kiedy
pliki z logami systemowymi s± ju¿ du¿e.

%description -l tr
Logarch çok fazla sayýda günlük dosyasý üreten sistemlerin yönetimini
kolaylaþtýrmak için tasarlanmýþtýr. Kayýt dosyalarýnýn otomatik olarak
yönlendirilmesini, sýkýþtýrýlmasýný, silinmesiný ve mektup olarak
yollanmasýný saðlar. Her dosya günlük, haftalýk, aylýk olarak ya da
çok büyük boyutlara ulaþtýðýnda iþlenebilir.

%prep
%setup -q
%patch -p0

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README examples/logarch.d/*
%attr(755,root,root) %{_sbindir}/logarch
%attr(750,root,root) %dir %{_sysconfdir}/logarch.d
#%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/logarch
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(750,root,root) %dir /var/log/archiv
