Name:           nsca_manager
Version:        1.0
Release:        1%{?dist}
Summary:        nsca_manager

Group:          Utilities
License:        GPL
URL:            www.evam.com
Source0:        nsca_manager-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  nagios
Requires:       nagios

%description
nsca_manager

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_manager
mkdir $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_manager/nsca_manager
tar xvfz  %{SOURCE0} && cp -R nsca_manager-1.0/nsca_manager $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_manager
install nsca_manager-1.0/nsca_manager/nsca_manager $RPM_BUILD_ROOT/usr/libexec/nagios/plugins/nsca_manager/nsca_manager/nsca_manager

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir /usr/libexec/nagios/plugins/nsca_manager
%defattr(-,root,root,-)
/usr/libexec/nagios/plugins/nsca_manager/nsca_manager/nsca_manager
