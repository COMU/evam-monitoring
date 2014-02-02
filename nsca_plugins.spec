Name:           nsca_plugins
Version:        1.0
Release:        1%{?dist}
Summary:        EVAM nsca plugins

Group:          Utilities
License:        GPL
URL:            www.evam.com
Source0:        nsca_plugins-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  nagios
Requires:       nagios

%description
EVAM icin kullanilan nsca eklentiler

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf
tar xvfz  %{SOURCE0} && cp -R nsca_plugins-1.0/nsca_plugins $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins
install nsca_plugins-1.0/nsca_plugins/match_errors/check_evam_engine_errors_match $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/check_evam_engine_errors_match
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/check_intellica_query $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/check_intellica_query
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/sqlScriptRunner.jar $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/sqlScriptRunner.jar
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/log4j.properties $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/log4j.properties


%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir /usr/libexec/nagios/plugins/nsca_plugins
%defattr(-,root,root,-)
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/check_evam_engine_errors_match
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/check_intellica_query
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/sqlScriptRunner.jar
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/log4j.properties
