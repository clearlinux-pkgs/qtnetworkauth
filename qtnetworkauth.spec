#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtnetworkauth
Version  : 5.10.0
Release  : 1
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.0/submodules/qtnetworkauth-everywhere-src-5.10.0.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.0/submodules/qtnetworkauth-everywhere-src-5.10.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0
Requires: qtnetworkauth-lib
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev

%description
No detailed description available

%package dev
Summary: dev components for the qtnetworkauth package.
Group: Development
Requires: qtnetworkauth-lib
Provides: qtnetworkauth-devel

%description dev
dev components for the qtnetworkauth package.


%package lib
Summary: lib components for the qtnetworkauth package.
Group: Libraries

%description lib
lib components for the qtnetworkauth package.


%prep
%setup -q -n qtnetworkauth-everywhere-src-5.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
`pkg-config --variable=host_bins Qt5Core $(sed -n '/MODULE_VERSION */s///p' .qmake.conf 2>/dev/null)`/qmake --
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qabstractoauth2_p.h
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qabstractoauth_p.h
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qabstractoauthreplyhandler_p.h
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qoauth1_p.h
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qoauth1signature_p.h
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h
/usr/include/qt5/QtNetworkAuth/5.10.0/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h
/usr/include/qt5/QtNetworkAuth/QAbstractOAuth
/usr/include/qt5/QtNetworkAuth/QAbstractOAuth2
/usr/include/qt5/QtNetworkAuth/QAbstractOAuthReplyHandler
/usr/include/qt5/QtNetworkAuth/QOAuth1
/usr/include/qt5/QtNetworkAuth/QOAuth1Signature
/usr/include/qt5/QtNetworkAuth/QOAuth2AuthorizationCodeFlow
/usr/include/qt5/QtNetworkAuth/QOAuthHttpServerReplyHandler
/usr/include/qt5/QtNetworkAuth/QOAuthOobReplyHandler
/usr/include/qt5/QtNetworkAuth/QtNetworkAuth
/usr/include/qt5/QtNetworkAuth/QtNetworkAuthDepends
/usr/include/qt5/QtNetworkAuth/QtNetworkAuthVersion
/usr/include/qt5/QtNetworkAuth/qabstractoauth.h
/usr/include/qt5/QtNetworkAuth/qabstractoauth2.h
/usr/include/qt5/QtNetworkAuth/qabstractoauthreplyhandler.h
/usr/include/qt5/QtNetworkAuth/qoauth1.h
/usr/include/qt5/QtNetworkAuth/qoauth1signature.h
/usr/include/qt5/QtNetworkAuth/qoauth2authorizationcodeflow.h
/usr/include/qt5/QtNetworkAuth/qoauthglobal.h
/usr/include/qt5/QtNetworkAuth/qoauthhttpserverreplyhandler.h
/usr/include/qt5/QtNetworkAuth/qoauthoobreplyhandler.h
/usr/include/qt5/QtNetworkAuth/qtnetworkauthversion.h
/usr/lib64/cmake/Qt5NetworkAuth/Qt5NetworkAuthConfig.cmake
/usr/lib64/cmake/Qt5NetworkAuth/Qt5NetworkAuthConfigVersion.cmake
/usr/lib64/libQt5NetworkAuth.la
/usr/lib64/libQt5NetworkAuth.prl
/usr/lib64/libQt5NetworkAuth.so
/usr/lib64/pkgconfig/Qt5NetworkAuth.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_networkauth.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_networkauth_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5NetworkAuth.so.5
/usr/lib64/libQt5NetworkAuth.so.5.10
/usr/lib64/libQt5NetworkAuth.so.5.10.0
