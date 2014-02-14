Name:           evam-nsca-manager
Version:        1.0
Release:        1%{?dist}
Summary:        EVAM nsca management utility

Group:          Utilities
License:        GPL
URL:            www.evam.com
Source0:        evam-nsca-manager-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  filesystem
Requires:       evam-plugins, evam-nsca-plugins, cronie

%description
EVAM nsca manager nagios eklentilerinin cron aracılıgıyla otomatik olarak çalıstırılıp sonuclarının raporlanması icin kullanılan bir araçtır

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-manager
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-manager/nsca_manager
install -d $RPM_BUILD_ROOT/etc
mkdir $RPM_BUILD_ROOT/etc/cron.d
tar xvfz  %{SOURCE0} && cp -R evam-nsca-manager-1.0/nsca_manager $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-manager
install evam-nsca-manager-1.0/nsca_manager/nsca_manager $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-manager/nsca_manager/nsca_manager
install evam-nsca-manager-1.0/cron/nsca_manager $RPM_BUILD_ROOT/etc/cron.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,-)
/usr/libexec/nagios/plugins/evam-nsca-manager/nsca_manager/nsca_manager
/etc/cron.d/nsca_manager
