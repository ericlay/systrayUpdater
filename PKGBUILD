# Maintainer: Eric Lay <ericlaytm@gmail.com>
pkgname=systrayupdater
pkgver=r35.0af7ad3
pkgrel=1
pkgdesc="PyQt5 system tray applet to notify of available updates"
arch=('x86_64')
url="https://github.com/ericlay/$pkgname"
license=('GPL3')
depends=('python'
    'python-pyqt5'
	'python-yaml'
	'python-jaraco.functools'
	'pacman')
makedepends=('git')
optdepends=()
source=("git+https://github.com/ericlay/$pkgname.git")
md5sums=('SKIP')

pkgver(){
    cd "$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "$srcdir/$pkgname"
	install -Dm755 systrayUpdater -t "$pkgdir/usr/bin"
	install -Dm666 SysTrayUpdater.desktop -t "$pkgdir/usr/share/applications"
	install -Dm755 ./*.png systrayupdater.yml -t "$pkgdir/$HOME/.config/$pkgname"
}