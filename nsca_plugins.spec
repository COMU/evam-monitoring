Name:           nsca_plugins
Version:        1.0
Release:        1%{?dist}
Summary:        nsca_plugins

Group:          Utilities
License:        GPL
URL:            www.evam.com
Source0:        nsca_plugins-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bash
Requires:       bash

%description
nsca_plugins

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
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.smsc $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.smsc
install nsca_plugins-1.0/nsca_plugins/match_errors/check_evam_engine_errors_match $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/check_evam_engine_errorCount
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.daily $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.daily
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.engine $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.engine
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.ignored $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.ignored
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.known $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.known
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.monthly $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.monthly
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.mssql $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.mssql
install nsca_plugins-1.0/nsca_plugins/match_errors/errors.ods $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.ods
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/check_intellica_query $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/check_intellica_query
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/for_daily_queries.sh $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/for_daily_queries.sh
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/sqlScriptRunner.jar $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/sqlScriptRunner.jar
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/db.properties.0 $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.0
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/db.properties.1  $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.1
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/db.properties.2  $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.2
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/db.properties.3 $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.3
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/db.properties.4 $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.4
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/db.properties.5 $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.5
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/log4j.properties $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/log4j.properties
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/scenarios_hit_limit.sql $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/scenarios_hit_limit.sql
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/total_scenarios.sql $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_scenarios.sql
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/total_sms.sql  $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_sms.sql
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/total_users_1.sql $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_users_1.sql
install nsca_plugins-1.0/nsca_plugins/sql_script_runner/conf/total_users_2.sql $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_users_2.sql


%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir /usr/libexec/nagios/plugins/nsca_plugins
%defattr(-,root,root,-)
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/check_evam_engine_errors_match
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.smsc
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/check_evam_engine_errorCount
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.daily
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.engine
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.ignored
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.known
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.monthly
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.mssql
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/match_errors/errors.ods
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/check_intellica_query
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/for_daily_queries.sh
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/sqlScriptRunner.jar
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.0
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.1
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.2
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.3
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.4
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/db.properties.5
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/log4j.properties
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/scenarios_hit_limit.sql
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_scenarios.sql
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_sms.sql
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_users_1.sql
/usr/libexec/nagios/plugins/nsca_plugins/nsca_plugins/sql_script_runner/conf/total_users_2.sql
