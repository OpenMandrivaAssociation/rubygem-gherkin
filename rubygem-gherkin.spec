%define oname   gherkin

Name:       rubygem-%{oname}
Version:    2.11.5
Release:    3
Summary:    Fast Gherkin lexer/parser
Group:      Development/Ruby
License:    MIT
URL:        https://github.com/aslakhellesoy/gherkin
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRequires: rubygems
BuildRequires: ruby-devel
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rake-compiler) >= 0.7.1

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

#-------------------------------------------------------------------------------
%package        doc
Summary:    Documentation for %{name}
Group:      Development/Ruby
Requires:   %{name} = %{version}-%{release}

%description    doc
Documents, Rdoc & RI documentation for %{name}.
#-------------------------------------------------------------------------------

%prep
%setup -q
tar xmf data.tar.gz

%build
export RUBYOPT=-Ku
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/gherkin_lexer_*.so

%files          doc
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
