# Generated from gherkin-2.3.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	gherkin

Summary:	gherkin-2.3.4
Name:		rubygem-%{rbname}

Version:	2.3.4
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://github.com/aslakhellesoy/gherkin
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(rake)

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(features|ragel|spec|tasks)/'

%install
%gem_install
find -name %{buildroot} -name .gitignore |xargs rm -f

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/*.feature
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features/step_definitions
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/step_definitions/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features/support
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/support/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/ragel
%{ruby_gemdir}/gems/%{rbname}-%{version}/ragel/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/gherkin
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/gherkin/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/gherkin_lexer_*.so

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
