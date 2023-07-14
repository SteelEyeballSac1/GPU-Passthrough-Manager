Name: GPU-Passthrough-Manager
Release: 1
Version: 1.2.1
Summary: 'GPU passthrough made easy.'
License: GPL
Requires: python3
Conflicts: gpu-passthrough-manager
BuildRequires: gcc-c++ jsoncpp-devel git gtk3-devel
ExclusiveArch: x86_64
URL: https://github.com/uwzis/GPU-Passthrough-Manager/
Source0:  https://github.com/SteelEyeballSac1/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define debug_package %{nil}
%define srcdir %{_builddir}/gpu-passthrough-manager

%changelog
* Thu Jul 13 2017 - 1.2.1-1
- created specfile

%prep
%setup

%description
'GPU passthrough made easy'

%build
    export pkgdir="%{buildroot}"
    export srcdir="%{srcdir}"
    export _pkgname="%{_pkgname}"
    make

%install
    export pkgdir="%{buildroot}"
    export srcdir="%{srcdir}"
    export sourcedir="%{_builddir}/%{name}-%{version}"
    export _pkgname="%{_pkgname}"
    install -dm755 ${pkgdir}/usr/share/gpu-passthrough-manager
    install -dm755 ${pkgdir}/usr/share/polkit-1/actions
    cp -r --no-preserve=mode,ownership "${sourcedir}/icons" "${pkgdir}/usr/share/gpu-passthrough-manager"
    cp -r --no-preserve=mode,ownership "${sourcedir}/py" "${pkgdir}/usr/share/gpu-passthrough-manager"
    cp -r --no-preserve=mode,ownership "${sourcedir}/tools" "${pkgdir}/usr/share/gpu-passthrough-manager"
    cp --no-preserve=mode,ownership "${sourcedir}//style.css" "${pkgdir}/usr/share/gpu-passthrough-manager"
    cp --no-preserve=mode,ownership "${sourcedir}//tools/org.freedesktop.gpu-passthrough-manager.policy" "${pkgdir}/usr/share/polkit-1/actions/org.freedesktop.gpu-passthrough-manager.policy"
    install -Dm755 "${sourcedir}/GPUPM" "${pkgdir}/usr/share/gpu-passthrough-manager/GPUPM"
    install -Dm755 "${sourcedir}/tools/Reboot" "${pkgdir}/usr/share/gpu-passthrough-manager/tools/Reboot"
    rm -r "${pkgdir}/usr/share/gpu-passthrough-manager/tools/reboot.c"
    rm -r "${pkgdir}/usr/share/gpu-passthrough-manager/tools/apphandler.c"
    chmod +x "${pkgdir}/usr/share/gpu-passthrough-manager/GPUPM"
    chmod +x "${pkgdir}/usr/share/gpu-passthrough-manager/tools/Reboot"
    install -Dm755 "${sourcedir}/gpu-passthrough-manager" "${pkgdir}/usr/bin/gpu-passthrough-manager"	
    install -dm755 ${pkgdir}/usr/share/applications
    cp --no-preserve=mode,ownership "${sourcedir}/icons/GPU Passthrough Manager.desktop" "${pkgdir}/usr/share/applications/"
    install -dm755 ${pkgdir}/usr/share/doc/gpu-passthrough-manager
    cp --no-preserve=mode,ownership "${sourcedir}/README.md" "${pkgdir}/usr/share/doc/gpu-passthrough-manager"
    chmod 644 "${pkgdir}/usr/share/doc/gpu-passthrough-manager/README.md"
    
%files
"%{_usr}/share/gpu-passthrough-manager"
"%{_usr}/share/polkit-1/actions/org.freedesktop.gpu-passthrough-manager.policy"
"%{_usr}/share/applications/GPU Passthrough Manager.desktop"
"%{_usr}/share/doc/gpu-passthrough-manager/README.md"
"%{_usr}/bin/gpu-passthrough-manager"
