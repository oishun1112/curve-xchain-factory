from brownie import (
    ChildGauge,
    ChildGaugeFactory,
    RootGauge,
    RootGaugeFactory,
    accounts
)

DEPLOYER = accounts.load("test-2")

# Goerli network
INSURE = "0x09f0Ad07E7363557D077CF3e3BbaB9365DA533F6"
GAUGE_CONTROLLER = "0xbF77F0e2C4A860d5f98d06BbbBA85242D50D3311"
MINTER = "0x71Be077d20a6dc38C235BbCCEa900C36eE841F0E"
VE = "0x11e54A8BbE393D23Bf91af7afb61f3f9BC94d59A"

ANYCALL = "0x37414a8662bc1d25be3ee51fb27c2686e2490a89"  # not deployed on goerli


def deploy_root():
    factory = RootGaugeFactory.deploy(ANYCALL, DEPLOYER, {"from": DEPLOYER})
    gauge_impl = RootGauge.deploy(INSURE, GAUGE_CONTROLLER, MINTER, {"from": DEPLOYER})

    # set implementation
    factory.set_implementation(gauge_impl, {"from": DEPLOYER})


def deploy_child(crv_addr):
    factory = ChildGaugeFactory.deploy(ANYCALL, crv_addr, DEPLOYER, {"from": DEPLOYER})
    gauge_impl = ChildGauge.deploy(crv_addr, factory, {"from": DEPLOYER})

    # set implementation
    factory.set_implementation(gauge_impl, {"from": DEPLOYER})
