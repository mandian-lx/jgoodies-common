%global shortname common

Name:           jgoodies-common
Version:        1.1.1
Release:        5
Summary:        Common library shared by JGoodies libraries and applications

Group:          Development/Java
License:        BSD
URL:            http://www.jgoodies.com/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
Requires:       java
Requires:       jpackage-utils
BuildArch:      noarch

%description
The JGoodies Common library provides convenience code for other JGoodies
libraries and applications.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

# Delete prebuild JARs
find -name "*.jar" -exec rm -f {} \;

# Remove DOS line endings
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed 's|\r||g' $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
ant \
  jar \
  javadoc


%install
install -Dpm 0644 build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -a build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.html RELEASE-NOTES.txt
%{_javadir}/*.jar


%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}/




%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 1.1.1-4
+ Revision: 734048
- rebuild
- imported package jgoodies-common

