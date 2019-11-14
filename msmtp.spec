#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x03A2A4AB1E32FD34 (marlam@marlam.de)
#
Name     : msmtp
Version  : 1.8.3
Release  : 22
URL      : https://marlam.de/msmtp/releases/msmtp-1.8.3.tar.xz
Source0  : https://marlam.de/msmtp/releases/msmtp-1.8.3.tar.xz
Source1 : https://marlam.de/msmtp/releases/msmtp-1.8.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: msmtp-bin = %{version}-%{release}
Requires: msmtp-info = %{version}-%{release}
Requires: msmtp-license = %{version}-%{release}
Requires: msmtp-locales = %{version}-%{release}
Requires: msmtp-man = %{version}-%{release}
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libidn2)
BuildRequires : pkgconfig(openssl)

%description
msmtp is an SMTP client.
In the default mode, it transmits a mail to an SMTP server.

%package bin
Summary: bin components for the msmtp package.
Group: Binaries
Requires: msmtp-license = %{version}-%{release}

%description bin
bin components for the msmtp package.


%package info
Summary: info components for the msmtp package.
Group: Default

%description info
info components for the msmtp package.


%package license
Summary: license components for the msmtp package.
Group: Default

%description license
license components for the msmtp package.


%package locales
Summary: locales components for the msmtp package.
Group: Default

%description locales
locales components for the msmtp package.


%package man
Summary: man components for the msmtp package.
Group: Default

%description man
man components for the msmtp package.


%prep
%setup -q -n msmtp-1.8.3
cd %{_builddir}/msmtp-1.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573773935
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1573773935
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/msmtp
cp %{_builddir}/msmtp-1.8.3/COPYING %{buildroot}/usr/share/package-licenses/msmtp/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang msmtp
## install_append content
ln -s msmtp %{buildroot}%{_bindir}/sendmail
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/msmtp
/usr/bin/msmtpd
/usr/bin/sendmail

%files info
%defattr(0644,root,root,0755)
/usr/share/info/msmtp.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/msmtp/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/msmtp.1
/usr/share/man/man1/msmtpd.1

%files locales -f msmtp.lang
%defattr(-,root,root,-)

