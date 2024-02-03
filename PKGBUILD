# Maintainer: frenzieddoll <frenziddoll@gmail.com>
pkgname=argon_one_fan_control
pkgver=1.0
pkgrel=1
pkgdesc="Argon One Fan Control Scripts"
url='https://github.com/frenzieddoll/argon_one_fan_control'
arch=('aarch64')
license=('GPL3')
depends=('i2c-tools' 'python>=3.3' 'python-smbus-git')

source=(
  "${url}/argonone.py"
  "${url}/argononed.service"
  )

package() {
  install -Dm755 "${srcdir}"/argonone.py "${pkgdir}"/opt/argonone/argonone.py
  install -Dm644 "${srcdir}"/argononed.service "${pkgdir}"/usr/lib/systemd/system/argononed.service
}
