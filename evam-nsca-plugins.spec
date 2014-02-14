Name:           evam-nsca-plugins
Version:        1.0
Release:        1%{?dist}
Summary:        EVAM nsca plugins

License:        GPL
URL:            www.evam.com
Source0:        evam-nsca-plugins-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  filesystem
Requires:       java-1.7.0-openjdk

%description
EVAM icin kullanilan nsca eklentiler

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/sql_script_runner
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/match_errors
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/sql_script_runner/conf
tar xvfz  %{SOURCE0} && cp -R evam-nsca-plugins-1.0/nsca_plugins $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins
install evam-nsca-plugins-1.0/nsca_plugins/match_errors/check_evam_engine_errors_match $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/match_errors/check_evam_engine_errors_match
install evam-nsca-plugins-1.0/nsca_plugins/sql_script_runner/check_intellica_query $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/sql_script_runner/check_intellica_query
install evam-nsca-plugins-1.0/nsca_plugins/sql_script_runner/sqlScriptRunner.jar $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/sql_script_runner/sqlScriptRunner.jar
install evam-nsca-plugins-1.0/nsca_plugins/sql_script_runner/conf/log4j.properties $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/evam-nsca-plugins/nsca_plugins/sql_script_runner/conf/log4j.properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
#%dir /usr/libexec/nagios/plugins/nsca_plugins
%defattr(644,root,root,-)
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/check_evam_engine_errors_match
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/check_intellica_query
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/sqlScriptRunner.jar
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/log4j.properties
