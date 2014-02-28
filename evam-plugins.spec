Name:           evam-plugins
Version:        1.0
Release:        1%{?dist}
Summary:        EVAM evam plugins utility
Group:          Applications/System

License:        GPL
URL:            http://www.evam.com
Source0:        http://members.comu.edu.tr/nyucel/evam/evam-plugins-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  nagios
Requires:       nagios

%description
EVAM evam plugins nagios eklentilerinin cron aracılıgıyla otomatik olarak çalıstırılıp sonuclarının raporlanması icin kullanılan bir araçtır

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins
tar xvfz  %{SOURCE0} && cp -R evam-plugins $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam
install evam-plugins-%{version}/evam-plugins/check_evam_engine_errorCount $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_errorCount
install evam-plugins-%{version}/evam-plugins/check_evam_engine_logLineCount $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_logLineCount
install evam-plugins-%{version}/evam-plugins/check_evam_engine_proc  $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_proc
install evam-plugins-%{version}/evam-plugins/check_evam_engine_qsize $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_qsize
install evam-plugins-%{version}/evam-plugins/check_evam_engine_threadStatus $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_threadStatus
install evam-plugins-%{version}/evam-plugins/check_evam_engine_warningCount $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_warningCount
install evam-plugins-%{version}/evam-plugins/check_evam_listener_proc $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_listener_proc
install evam-plugins-%{version}/evam-plugins/check_intellica_cpu $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_cpu
install evam-plugins-%{version}/evam-plugins/check_intellica_disk $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_disk
install evam-plugins-%{version}/evam-plugins/check_intellica_file_count $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_file_count
install evam-plugins-%{version}/evam-plugins/check_intellica_file_time $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_file_time
install evam-plugins-%{version}/evam-plugins/check_intellica_memory $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_memory
mkdir $RPM_BUILD_ROOT/etc
install evam-plugins-%{version}/evam.conf $RPM_BUILD_ROOT/etc/evam.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
#%dir /usr/libexec/nagios/plugins/evam
%defattr(644,root,root,-)
/etc/evam.conf
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_errorCount
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_logLineCount
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_proc
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_qsize
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_threadStatus
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_engine_warningCount
/usr/libexec/nagios/plugins/evam/evam-plugins/check_evam_listener_proc
/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_cpu
/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_disk
/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_file_count
/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_file_time
/usr/libexec/nagios/plugins/evam/evam-plugins/check_intellica_memory

%post
chmod 755 -R /usr/libexec/nagios/plugins/evam/evam-plugins
