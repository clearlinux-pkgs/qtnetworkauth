#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtnetworkauth
Version  : 5.14.2
Release  : 20
URL      : https://download.qt.io/official_releases/qt/5.14/5.14.2/submodules/qtnetworkauth-everywhere-src-5.14.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.14/5.14.2/submodules/qtnetworkauth-everywhere-src-5.14.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0
Requires: qtnetworkauth-lib = %{version}-%{release}
Requires: qtnetworkauth-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)

%description
No detailed description available

%package dev
Summary: dev components for the qtnetworkauth package.
Group: Development
Requires: qtnetworkauth-lib = %{version}-%{release}
Provides: qtnetworkauth-devel = %{version}-%{release}
Requires: qtnetworkauth = %{version}-%{release}

%description dev
dev components for the qtnetworkauth package.


%package examples
Summary: examples components for the qtnetworkauth package.
Group: Default
Requires: qtnetworkauth-dev = %{version}-%{release}

%description examples
examples components for the qtnetworkauth package.


%package lib
Summary: lib components for the qtnetworkauth package.
Group: Libraries
Requires: qtnetworkauth-license = %{version}-%{release}

%description lib
lib components for the qtnetworkauth package.


%package license
Summary: license components for the qtnetworkauth package.
Group: Default

%description license
license components for the qtnetworkauth package.


%prep
%setup -q -n qtnetworkauth-everywhere-src-5.14.2
cd %{_builddir}/qtnetworkauth-everywhere-src-5.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1586201098
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtnetworkauth
cp %{_builddir}/qtnetworkauth-everywhere-src-5.14.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtnetworkauth/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtnetworkauth-everywhere-src-5.14.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtnetworkauth/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtnetworkauth-everywhere-src-5.14.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtnetworkauth/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qabstractoauth2_p.h
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qabstractoauth_p.h
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qabstractoauthreplyhandler_p.h
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qoauth1_p.h
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qoauth1signature_p.h
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h
/usr/include/qt5/QtNetworkAuth/5.14.2/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h
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
/usr/lib64/libQt5NetworkAuth.prl
/usr/lib64/libQt5NetworkAuth.so
/usr/lib64/pkgconfig/Qt5NetworkAuth.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_networkauth.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_networkauth_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/oauth/oauth.pro
/usr/share/qt5/examples/oauth/redditclient/main.cpp
/usr/share/qt5/examples/oauth/redditclient/redditclient.pro
/usr/share/qt5/examples/oauth/redditclient/redditmodel.cpp
/usr/share/qt5/examples/oauth/redditclient/redditmodel.h
/usr/share/qt5/examples/oauth/redditclient/redditwrapper.cpp
/usr/share/qt5/examples/oauth/redditclient/redditwrapper.h
/usr/share/qt5/examples/oauth/twittertimeline/main.cpp
/usr/share/qt5/examples/oauth/twittertimeline/twitter.cpp
/usr/share/qt5/examples/oauth/twittertimeline/twitter.h
/usr/share/qt5/examples/oauth/twittertimeline/twitterdialog.ui
/usr/share/qt5/examples/oauth/twittertimeline/twittertimeline.pro
/usr/share/qt5/examples/oauth/twittertimeline/twittertimelinemodel.cpp
/usr/share/qt5/examples/oauth/twittertimeline/twittertimelinemodel.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5NetworkAuth.so.5
/usr/lib64/libQt5NetworkAuth.so.5.14
/usr/lib64/libQt5NetworkAuth.so.5.14.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtnetworkauth/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtnetworkauth/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtnetworkauth/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
