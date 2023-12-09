# Maintainer: Eric Lay <ericlaytm@gmail.com>
pkgname=systrayupdater
pkgver=r47.a550ac3
pkgrel=1
pkgdesc="PyQt5 system tray applet notifier of available updates"
arch=('x86_64')
url="https://github.com/ericlay/$pkgname"
license=('GPL3')
depends=('python'
    'python-pyqt5'
	'python-yaml'
	'hicolor-icon-theme'
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
	install -Dm755 systray-updater -t "$pkgdir/usr/bin"
	install -Dm755 config.yml -t "$pkgdir/etc/$pkgname"
	install -Dm666 systrayupdater.desktop -t "$pkgdir/usr/share/applications"
	install -Dm644 ./*.svg -t "$pkgdir/usr/share/icons/hicolor/symbolic/apps"
}
