{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\wnsau'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<selenium.webdriver.chrome.webdriver.WebDriver (session=\"cf9047da91cfb03de7ebb4c560746fa4\")>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "driver = webdriver.Chrome('chromedriver')\n",
    "driver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.amazon.com/'\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input input\n"
     ]
    }
   ],
   "source": [
    "sel_search = driver.find_element_by_xpath('//*[@id=\"twotabsearchtextbox\"]')\n",
    "sel_btn = driver.find_element_by_xpath('//*[@id=\"nav-search-submit-button\"]')\n",
    "\n",
    "print(sel_search.tag_name, sel_btn.tag_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "sel_search.clear()\n",
    "sel_search.send_keys('earphones')\n",
    "sel_btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0870194129TKFEDZ8MAO&url=%2FHeadphones-Bluetooth-Reduction-Microphone-Compatible%2Fdp%2FB095RHGZKB%2Fref%3Dsr_1_1_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-1-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf\n"
     ]
    }
   ],
   "source": [
    "sel_earphone = driver.find_element_by_xpath('//*[@id=\"search\"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/h2/a')\n",
    "print(sel_earphone.get_attribute('href'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://www.amazon.com/ref=nav_logo', 'https://www.amazon.com/gp/customer-preferences/select-language/ref=topnav_lang_ais?preferencesReturnUrl=%2Fs%3Fk%3Dearphones%26ref%3Dnb_sb_noss', 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dearphones%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&', 'https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first', 'https://www.amazon.com/gp/cart/view.html?ref_=nav_cart', 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dearphones%26ref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&', 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2Fref%3Dnb_sb_noss%2F%3F_encoding%3DUTF8%26field-keywords%3Dearphones%26url%3Dsearch-alias%253Daps%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&', 'https://www.amazon.com/gp/registry/wishlist?triggerElementID=createList&ref_=nav_ListFlyout_create', 'https://www.amazon.com/gp/registry/search?ref_=nav_ListFlyout_find', 'https://www.amazon.com/gp/clpf?ref_=nav_ListFlyout_smi_se_ya_lll_ll', 'https://www.amazon.com/gp/css/homepage.html?ref_=nav_AccountFlyout_ya', 'https://www.amazon.com/gp/css/order-history?ref_=nav_AccountFlyout_orders', 'https://www.amazon.com/gp/yourstore?ref_=nav_AccountFlyout_recs', 'https://www.amazon.com/gp/history?ref_=nav_AccountFlyout_browsinghistory', 'https://www.amazon.com/gp/video/watchlist?ref_=nav_AccountFlyout_ywl', 'https://www.amazon.com/gp/video/library?ref_=nav_AccountFlyout_yvl', 'https://www.amazon.com/gp/kindle/ku/ku_central?ref_=nav_AccountFlyout_ku', 'https://www.amazon.com/hz/mycd/myx?ref_=nav_AccountFlyout_myk', 'https://www.amazon.com/gp/subscribe-and-save/manager/viewsubscriptions?ref_=nav_AccountFlyout_sns', 'https://www.amazon.com/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions', 'https://www.amazon.com/gp/dmusic/mp3/player?ref_=nav_AccountFlyout_cldplyr', 'javascript: void(0)', 'https://www.amazon.com/international-sales-offers/b/?ie=UTF8&node=15529609011&ref_=nav_cs_gb_intl_52df97a2eee74206a8343034e85cd058', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice_2bf4fe8c5ec54e6bae2d1c24043f012b', 'https://www.amazon.com/gift-cards/b/?ie=UTF8&node=2238192011&ref_=nav_cs_gc_4fb606b1a14b44e4823e00c03fc71f47', 'https://www.amazon.com/gp/browse.html?node=16115931011&ref_=nav_cs_registry_1c421982e26d4ec48ca364be68f201b5', 'https://www.amazon.com/b/?_encoding=UTF8&ld=AZUSSOA-sell&node=12766669011&ref_=nav_cs_sell_9321d964d1ab428b8d83e204c043fc01', 'https://www.amazon.com/gp/help/customer/accessibility', 'https://blog.aboutamazon.com/company-news/amazons-actions-to-help-employees-communities-and-customers-affected-by-covid-19/?_encoding=UTF8&token=GW&utm_content=COVID-19_roundup&utm_medium=swm&utm_source=gateway&utm_term=gw03162020&ref_=nav_swm_undefined&pf_rd_p=cf6260e5-93a9-45ad-9653-d1fc95751fac&pf_rd_s=nav-sitewide-msg-text-export&pf_rd_t=4201&pf_rd_i=navbar-4201&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=N9411CP5TYYQ3W9JDBB4', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/s/ref=sxts_sxts_ref_scx_alster_0?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097488011&nav_sdd=aps&pd_rd_w=LZOaL&pf_rd_p=04238f10-283f-4984-9ede-1a6d0468e860&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=a35f95b9-c155-4cd0-bb10-1259bbcf9597&pd_rd_wg=mULH2&qid=1624238885', 'https://www.amazon.com/s/ref=sxts_sxts_ref_scx_alster_1?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A2266981011&nav_sdd=aps&pd_rd_w=LZOaL&pf_rd_p=04238f10-283f-4984-9ede-1a6d0468e860&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=a35f95b9-c155-4cd0-bb10-1259bbcf9597&pd_rd_wg=mULH2&qid=1624238885', 'https://www.amazon.com/s/ref=sxts_sxts_ref_scx_alster_2?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A2266980011&nav_sdd=aps&pd_rd_w=LZOaL&pf_rd_p=04238f10-283f-4984-9ede-1a6d0468e860&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=a35f95b9-c155-4cd0-bb10-1259bbcf9597&pd_rd_wg=mULH2&qid=1624238885', 'https://www.amazon.com/s/ref=sxts_sxts_ref_scx_alster_3?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097493011&nav_sdd=aps&pd_rd_w=LZOaL&pf_rd_p=04238f10-283f-4984-9ede-1a6d0468e860&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=a35f95b9-c155-4cd0-bb10-1259bbcf9597&pd_rd_wg=mULH2&qid=1624238885', 'https://www.amazon.com/s/ref=sxts_sxts_ref_scx_alster_4?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A6131843011&nav_sdd=aps&pd_rd_w=LZOaL&pf_rd_p=04238f10-283f-4984-9ede-1a6d0468e860&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=a35f95b9-c155-4cd0-bb10-1259bbcf9597&pd_rd_wg=mULH2&qid=1624238885', 'https://www.amazon.com/s/ref=sxts_sxts_ref_scx_alster_5?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A509316&nav_sdd=aps&pd_rd_w=LZOaL&pf_rd_p=04238f10-283f-4984-9ede-1a6d0468e860&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=a35f95b9-c155-4cd0-bb10-1259bbcf9597&pd_rd_wg=mULH2&qid=1624238885', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0870194129TKFEDZ8MAO&url=%2FHeadphones-Bluetooth-Reduction-Microphone-Compatible%2Fdp%2FB095RHGZKB%2Fref%3Dsr_1_1_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-1-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0870194129TKFEDZ8MAO&url=%2FHeadphones-Bluetooth-Reduction-Microphone-Compatible%2Fdp%2FB095RHGZKB%2Fref%3Dsr_1_1_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-1-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0870194129TKFEDZ8MAO&url=%2FHeadphones-Bluetooth-Reduction-Microphone-Compatible%2Fdp%2FB095RHGZKB%2Fref%3Dsr_1_1_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-1-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0599357W1M1A4X1IR4S&url=%2FKLIM-Fusion-Earbuds-Audio-Ear%2Fdp%2FB0736SCQ4X%2Fref%3Dsr_1_2_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-2-spons%26psc%3D1%26smid%3DA1Y2HVFT1GWBYK&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0599357W1M1A4X1IR4S&url=%2FKLIM-Fusion-Earbuds-Audio-Ear%2Fdp%2FB0736SCQ4X%2Fref%3Dsr_1_2_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-2-spons%26psc%3D1%26smid%3DA1Y2HVFT1GWBYK&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf', 'javascript:void(0)', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0599357W1M1A4X1IR4S&url=%2FKLIM-Fusion-Earbuds-Audio-Ear%2Fdp%2FB0736SCQ4X%2Fref%3Dsr_1_2_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-2-spons%26psc%3D1%26smid%3DA1Y2HVFT1GWBYK&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf#customerReviews', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0599357W1M1A4X1IR4S&url=%2FKLIM-Fusion-Earbuds-Audio-Ear%2Fdp%2FB0736SCQ4X%2Fref%3Dsr_1_2_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-2-spons%26psc%3D1%26smid%3DA1Y2HVFT1GWBYK&qualifier=1624238885&id=7714708109019064&widgetName=sp_atf', 'https://www.amazon.com/Apple-EarPods-3-5mm-Headphone-Plug/dp/B06X16Z7DZ/ref=sr_1_3?dchild=1&keywords=earphones&qid=1624238885&sr=8-3', 'https://www.amazon.com/Apple-EarPods-3-5mm-Headphone-Plug/dp/B06X16Z7DZ/ref=sr_1_3?dchild=1&keywords=earphones&qid=1624238885&sr=8-3', 'javascript:void(0)', 'https://www.amazon.com/Apple-EarPods-3-5mm-Headphone-Plug/dp/B06X16Z7DZ/ref=sr_1_3?dchild=1&keywords=earphones&qid=1624238885&sr=8-3#customerReviews', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=ice_ac_b_dpb?dchild=1&keywords=earphones&qid=1624238885&sr=8-4', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sr_1_4?dchild=1&keywords=earphones&qid=1624238885&sr=8-4', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sr_1_4?dchild=1&keywords=earphones&qid=1624238885&sr=8-4', 'javascript:void(0)', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sr_1_4?dchild=1&keywords=earphones&qid=1624238885&sr=8-4#customerReviews', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sr_1_4?dchild=1&keywords=earphones&qid=1624238885&sr=8-4', 'https://www.amazon.com/Axloie-Cancelling-Bluetooth-Headphones-Waterproof/dp/B08YDD1LCM/ref=sr_1_5?dchild=1&keywords=earphones&qid=1624238885&sr=8-5', 'https://www.amazon.com/Axloie-Cancelling-Bluetooth-Headphones-Waterproof/dp/B08YDD1LCM/ref=sr_1_5?dchild=1&keywords=earphones&qid=1624238885&sr=8-5', 'javascript:void(0)', 'https://www.amazon.com/Axloie-Cancelling-Bluetooth-Headphones-Waterproof/dp/B08YDD1LCM/ref=sr_1_5?dchild=1&keywords=earphones&qid=1624238885&sr=8-5#customerReviews', 'https://www.amazon.com/Axloie-Cancelling-Bluetooth-Headphones-Waterproof/dp/B08YDD1LCM/ref=sr_1_5?dchild=1&keywords=earphones&qid=1624238885&sr=8-5', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sxin_9_ac_d_rm?ac_md=0-0-ZWFycGhvbmVz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B0854F11JB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sxin_9_ac_d_rm?ac_md=0-0-ZWFycGhvbmVz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B0854F11JB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081', 'javascript:void(0)', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sxin_9_ac_d_rm?ac_md=0-0-ZWFycGhvbmVz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B0854F11JB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081#customerReviews', 'https://www.amazon.com/gp/goldbox/', 'https://www.amazon.com/Headphones-Microphone-Earphones-Compatible-Smartphones/dp/B0854F11JB/ref=sxin_9_ac_d_rm?ac_md=0-0-ZWFycGhvbmVz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B0854F11JB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sxin_9_ac_d_rm?ac_md=1-1-ZWFycGhvbmVzIGJsdWV0b290aCB3aXJlbGVzcw%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07RGZ5NKS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sxin_9_ac_d_rm?ac_md=1-1-ZWFycGhvbmVzIGJsdWV0b290aCB3aXJlbGVzcw%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07RGZ5NKS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081', 'javascript:void(0)', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sxin_9_ac_d_rm?ac_md=1-1-ZWFycGhvbmVzIGJsdWV0b290aCB3aXJlbGVzcw%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07RGZ5NKS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081#customerReviews', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sxin_9_ac_d_rm?ac_md=1-1-ZWFycGhvbmVzIGJsdWV0b290aCB3aXJlbGVzcw%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07RGZ5NKS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/Skullcandy-Dime-True-Wireless-Earbud/dp/B08X1QWB9W/ref=sxin_9_ac_d_rm?ac_md=3-2-c2t1bGxjYW5keSBlYXJidWRz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08X1QWB9W&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-3-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/Skullcandy-Dime-True-Wireless-Earbud/dp/B08X1QWB9W/ref=sxin_9_ac_d_rm?ac_md=3-2-c2t1bGxjYW5keSBlYXJidWRz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08X1QWB9W&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-3-12d4272d-8adb-4121-8624-135149aa9081', 'javascript:void(0)', 'https://www.amazon.com/Skullcandy-Dime-True-Wireless-Earbud/dp/B08X1QWB9W/ref=sxin_9_ac_d_rm?ac_md=3-2-c2t1bGxjYW5keSBlYXJidWRz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08X1QWB9W&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-3-12d4272d-8adb-4121-8624-135149aa9081#customerReviews', 'https://www.amazon.com/Skullcandy-Dime-True-Wireless-Earbud/dp/B08X1QWB9W/ref=sxin_9_ac_d_rm?ac_md=3-2-c2t1bGxjYW5keSBlYXJidWRz-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08X1QWB9W&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-3-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/Sony-MDREX15AP-B-Black/dp/B00JG2WRUO/ref=sxin_9_ac_d_rm?ac_md=4-3-c29ueSBlYXJwaG9uZQ%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B00JG2WRUO&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-4-12d4272d-8adb-4121-8624-135149aa9081', 'https://www.amazon.com/Sony-MDREX15AP-B-Black/dp/B00JG2WRUO/ref=sxin_9_ac_d_rm?ac_md=4-3-c29ueSBlYXJwaG9uZQ%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B00JG2WRUO&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-4-12d4272d-8adb-4121-8624-135149aa9081', 'javascript:void(0)', 'https://www.amazon.com/Sony-MDREX15AP-B-Black/dp/B00JG2WRUO/ref=sxin_9_ac_d_rm?ac_md=4-3-c29ueSBlYXJwaG9uZQ%3D%3D-ac_d_rm&cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B00JG2WRUO&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=BZ3Fv&pd_rd_wg=PWdKE&pf_rd_p=1493ce18-a74b-4311-9662-82d8e55e9a65&pf_rd_r=N9411CP5TYYQ3W9JDBB4&psc=1&qid=1624238885&sr=1-4-12d4272d-8adb-4121-8624-135149aa9081#customerReviews', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/profile/amzn1.account.AE3IWK4ANZHZBXFR2QWIS4LF4HQA/ref=sxin_10?linkCode=oas&asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contenttype=article&cv_ct_pg=search&cv_ct_wn=osp-single-source-earns-comm&cv_ct_we=contributor-profile&pd_rd_w=AeKGS&pf_rd_p=2a3243ce-188f-426b-9a7c-cd22d207971e&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_wg=PWdKE&qid=1624238885&cv_ct_cx=earphones', 'https://www.amazon.com/ospublishing/onsite-associates/info?linkCode=oas&asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contenttype=article&cv_ct_pg=search&cv_ct_wn=osp-single-source-earns-comm&cv_ct_we=disclaimer', 'https://www.amazon.com/ospublishing/story/8a5b8b4b-e51e-41fe-86cd-41d640824b9c/ref=sxin_10?cv_ct_pg=search&cv_ct_wn=osp-single-source-earns-comm&linkCode=oas&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_we=article-page&qid=1624238885&ascsubtag=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&pf_rd_p=2a3243ce-188f-426b-9a7c-cd22d207971e&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_wg=PWdKE&pd_rd_w=AeKGS&tag=bestgiftszmg-20&asc_contenttype=article&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&cv_ct_cx=earphones', 'https://www.amazon.com/Wireless-Waterproof-Bluetooth-Headphones-Playback/dp/B085RLPPS4/ref=sxin_10?asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&creativeASIN=B085RLPPS4&cv_ct_cx=earphones&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=earphones&linkCode=oas&pd_rd_i=B085RLPPS4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=AeKGS&pd_rd_wg=PWdKE&pf_rd_p=2a3243ce-188f-426b-9a7c-cd22d207971e&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-64f3a41a-73ca-403a-923c-8152c45485fe&tag=bestgiftszmg-20', 'https://www.amazon.com/Wireless-Waterproof-Bluetooth-Headphones-Playback/dp/B085RLPPS4/ref=sxin_10?asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&creativeASIN=B085RLPPS4&cv_ct_cx=earphones&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=earphones&linkCode=oas&pd_rd_i=B085RLPPS4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=AeKGS&pd_rd_wg=PWdKE&pf_rd_p=2a3243ce-188f-426b-9a7c-cd22d207971e&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-64f3a41a-73ca-403a-923c-8152c45485fe&tag=bestgiftszmg-20', 'javascript:void(0)', 'https://www.amazon.com/Wireless-Waterproof-Bluetooth-Headphones-Playback/dp/B085RLPPS4/ref=sxin_10?asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&creativeASIN=B085RLPPS4&cv_ct_cx=earphones&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=earphones&linkCode=oas&pd_rd_i=B085RLPPS4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=AeKGS&pd_rd_wg=PWdKE&pf_rd_p=2a3243ce-188f-426b-9a7c-cd22d207971e&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-64f3a41a-73ca-403a-923c-8152c45485fe&tag=bestgiftszmg-20#customerReviews', 'https://www.amazon.com/Wireless-Waterproof-Bluetooth-Headphones-Playback/dp/B085RLPPS4/ref=sxin_10?asc_contentid=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&creativeASIN=B085RLPPS4&cv_ct_cx=earphones&cv_ct_id=amzn1.osa.8a5b8b4b-e51e-41fe-86cd-41d640824b9c.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=earphones&linkCode=oas&pd_rd_i=B085RLPPS4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=AeKGS&pd_rd_wg=PWdKE&pf_rd_p=2a3243ce-188f-426b-9a7c-cd22d207971e&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-64f3a41a-73ca-403a-923c-8152c45485fe&tag=bestgiftszmg-20', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/s/ref=sxin_trfob?rh=n%3A17602470011&k=earphones&i=aps&srs=17602470011&pd_rd_w=sJsiT&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_wg=PWdKE&qid=1624238885', 'https://www.amazon.com/AmazonBasics-Ear-Headphones-Mic-Black/dp/B07HH1QSLB/ref=sxin_11_trfob_0?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07HH1QSLB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/AmazonBasics-Ear-Headphones-Mic-Black/dp/B07HH1QSLB/ref=sxin_11_trfob_0?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07HH1QSLB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/AmazonBasics-Ear-Headphones-Mic-Black/dp/B07HH1QSLB/ref=sxin_11_trfob_0?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07HH1QSLB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/AmazonBasics-Ear-Headphones-Mic-Black/dp/B07HH1QSLB/ref=sxin_11_trfob_0?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07HH1QSLB&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-1-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Cancelling-Headphones-Lightweight-Srhythm-Bluetooth/dp/B07F62W3TQ/ref=sxin_11_trfob_2?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07F62W3TQ&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-2-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Cancelling-Headphones-Lightweight-Srhythm-Bluetooth/dp/B07F62W3TQ/ref=sxin_11_trfob_2?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07F62W3TQ&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-2-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/Cancelling-Headphones-Lightweight-Srhythm-Bluetooth/dp/B07F62W3TQ/ref=sxin_11_trfob_2?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07F62W3TQ&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-2-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/Cancelling-Headphones-Lightweight-Srhythm-Bluetooth/dp/B07F62W3TQ/ref=sxin_11_trfob_2?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B07F62W3TQ&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-2-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Earphones-iFory-Earbuds-Headphones-Compatible/dp/B08C5GL91C/ref=sxin_11_trfob_3?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08C5GL91C&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-3-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Earphones-iFory-Earbuds-Headphones-Compatible/dp/B08C5GL91C/ref=sxin_11_trfob_3?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08C5GL91C&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-3-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/Earphones-iFory-Earbuds-Headphones-Compatible/dp/B08C5GL91C/ref=sxin_11_trfob_3?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08C5GL91C&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-3-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/Earphones-iFory-Earbuds-Headphones-Compatible/dp/B08C5GL91C/ref=sxin_11_trfob_3?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08C5GL91C&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-3-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Wireless-Headphones-Bluetooth-Earphones-Cancelling/dp/B091GHBXWG/ref=sxin_11_trfob_4?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B091GHBXWG&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-4-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Wireless-Headphones-Bluetooth-Earphones-Cancelling/dp/B091GHBXWG/ref=sxin_11_trfob_4?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B091GHBXWG&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-4-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/Wireless-Headphones-Bluetooth-Earphones-Cancelling/dp/B091GHBXWG/ref=sxin_11_trfob_4?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B091GHBXWG&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-4-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/Wireless-Headphones-Bluetooth-Earphones-Cancelling/dp/B091GHBXWG/ref=sxin_11_trfob_4?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B091GHBXWG&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-4-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Bluetooth-Headphones-Earphones-Cancelling-Waterproof/dp/B08YYYZZNS/ref=sxin_11_trfob_5?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08YYYZZNS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&smid=A286UK7CCOWN1O&sr=1-5-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Bluetooth-Headphones-Earphones-Cancelling-Waterproof/dp/B08YYYZZNS/ref=sxin_11_trfob_5?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08YYYZZNS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&smid=A286UK7CCOWN1O&sr=1-5-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/Bluetooth-Headphones-Earphones-Cancelling-Waterproof/dp/B08YYYZZNS/ref=sxin_11_trfob_5?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08YYYZZNS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&smid=A286UK7CCOWN1O&sr=1-5-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/gp/goldbox/', 'https://www.amazon.com/Bluetooth-Headphones-Earphones-Cancelling-Waterproof/dp/B08YYYZZNS/ref=sxin_11_trfob_5?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08YYYZZNS&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&smid=A286UK7CCOWN1O&sr=1-5-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/smpl-Wireless-Bluetooth-Earbuds-Premium/dp/B084VZRY8Y/ref=sxin_11_trfob_6?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B084VZRY8Y&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-6-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/smpl-Wireless-Bluetooth-Earbuds-Premium/dp/B084VZRY8Y/ref=sxin_11_trfob_6?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B084VZRY8Y&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-6-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/smpl-Wireless-Bluetooth-Earbuds-Premium/dp/B084VZRY8Y/ref=sxin_11_trfob_6?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B084VZRY8Y&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-6-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/Hadisala-Bluetooth-Headphones-Waterproof-Earphones/dp/B08DCV57L4/ref=sxin_11_trfob_7?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08DCV57L4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-7-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/Hadisala-Bluetooth-Headphones-Waterproof-Earphones/dp/B08DCV57L4/ref=sxin_11_trfob_7?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08DCV57L4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-7-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'javascript:void(0)', 'https://www.amazon.com/Hadisala-Bluetooth-Headphones-Waterproof-Earphones/dp/B08DCV57L4/ref=sxin_11_trfob_7?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08DCV57L4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-7-fcc74f9e-0165-48d2-a9e1-f41ea92a035c#customerReviews', 'https://www.amazon.com/Hadisala-Bluetooth-Headphones-Waterproof-Earphones/dp/B08DCV57L4/ref=sxin_11_trfob_7?cv_ct_cx=earphones&dchild=1&keywords=earphones&pd_rd_i=B08DCV57L4&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&pd_rd_w=sJsiT&pd_rd_wg=PWdKE&pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&pf_rd_r=N9411CP5TYYQ3W9JDBB4&qid=1624238885&sr=1-7-fcc74f9e-0165-48d2-a9e1-f41ea92a035c', 'https://www.amazon.com/gp/offer-listing/B08DCV57L4/ref=sxin_11_trfob_7_olp?pf_rd_p=6c6f0ed1-2306-4f6f-832e-d796b7d41a25&keywords=earphones&pd_rd_wg=PWdKE&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_i=B08DCV57L4&pd_rd_w=sJsiT&qid=1624238885&cv_ct_cx=earphones&pd_rd_r=7b9a6de9-d9ae-4093-9d53-b2c5773a379e&sr=1-7-fcc74f9e-0165-48d2-a9e1-f41ea92a035c&dchild=1', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sr_1_6?dchild=1&keywords=earphones&qid=1624238885&sr=8-6', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sr_1_6?dchild=1&keywords=earphones&qid=1624238885&sr=8-6', 'javascript:void(0)', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sr_1_6?dchild=1&keywords=earphones&qid=1624238885&sr=8-6#customerReviews', 'https://www.amazon.com/TOZO-T6-Bluetooth-Headphones-Waterproof/dp/B07RGZ5NKS/ref=sr_1_6?dchild=1&keywords=earphones&qid=1624238885&sr=8-6', 'https://www.amazon.com/gp/offer-listing/B07RGZ5NKS/ref=sr_1_6_olp?keywords=earphones&qid=1624238885&sr=8-6&dchild=1', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A00597812BIU05RH1JS67&url=%2FAmazonBasics-Earphones-Lightning-Connector-Certified%2Fdp%2FB07Q2GT5JP%2Fref%3Dsr_1_7_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-7-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A00597812BIU05RH1JS67&url=%2FAmazonBasics-Earphones-Lightning-Connector-Certified%2Fdp%2FB07Q2GT5JP%2Fref%3Dsr_1_7_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-7-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'javascript:void(0)', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A00597812BIU05RH1JS67&url=%2FAmazonBasics-Earphones-Lightning-Connector-Certified%2Fdp%2FB07Q2GT5JP%2Fref%3Dsr_1_7_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-7-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf#customerReviews', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A00597812BIU05RH1JS67&url=%2FAmazonBasics-Earphones-Lightning-Connector-Certified%2Fdp%2FB07Q2GT5JP%2Fref%3Dsr_1_7_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-7-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'https://www.amazon.com/TOZO-Bluetooth-Headphones-Earphones-Sweatproof/dp/B09539PPXF/ref=sr_1_8?dchild=1&keywords=earphones&qid=1624238885&sr=8-8', 'https://www.amazon.com/TOZO-Bluetooth-Headphones-Earphones-Sweatproof/dp/B09539PPXF/ref=sr_1_8?dchild=1&keywords=earphones&qid=1624238885&sr=8-8', 'javascript:void(0)', 'https://www.amazon.com/TOZO-Bluetooth-Headphones-Earphones-Sweatproof/dp/B09539PPXF/ref=sr_1_8?dchild=1&keywords=earphones&qid=1624238885&sr=8-8#customerReviews', 'https://www.amazon.com/TOZO-Bluetooth-Headphones-Earphones-Sweatproof/dp/B09539PPXF/ref=sr_1_8?dchild=1&keywords=earphones&qid=1624238885&sr=8-8', 'https://www.amazon.com/Earbuds-Headphones-Microphone-Earphones-Compatible/dp/B08Y72JWB4/ref=sr_1_9?dchild=1&keywords=earphones&qid=1624238885&sr=8-9', 'https://www.amazon.com/Earbuds-Headphones-Microphone-Earphones-Compatible/dp/B08Y72JWB4/ref=sr_1_9?dchild=1&keywords=earphones&qid=1624238885&sr=8-9', 'javascript:void(0)', 'https://www.amazon.com/Earbuds-Headphones-Microphone-Earphones-Compatible/dp/B08Y72JWB4/ref=sr_1_9?dchild=1&keywords=earphones&qid=1624238885&sr=8-9#customerReviews', 'https://www.amazon.com/Earbuds-Headphones-Microphone-Earphones-Compatible/dp/B08Y72JWB4/ref=sr_1_9?dchild=1&keywords=earphones&qid=1624238885&sr=8-9', 'https://www.amazon.com/Bluetooth-Headphones-Reduction-Waterproof-Earphones/dp/B092H1NQ19/ref=sr_1_10?dchild=1&keywords=earphones&qid=1624238885&sr=8-10', 'https://www.amazon.com/Bluetooth-Headphones-Reduction-Waterproof-Earphones/dp/B092H1NQ19/ref=sr_1_10?dchild=1&keywords=earphones&qid=1624238885&sr=8-10', 'javascript:void(0)', 'https://www.amazon.com/Bluetooth-Headphones-Reduction-Waterproof-Earphones/dp/B092H1NQ19/ref=sr_1_10?dchild=1&keywords=earphones&qid=1624238885&sr=8-10#customerReviews', 'https://www.amazon.com/Bluetooth-Headphones-Reduction-Waterproof-Earphones/dp/B092H1NQ19/ref=sr_1_10?dchild=1&keywords=earphones&qid=1624238885&sr=8-10', 'https://www.amazon.com/VEATOOL-Wireless-Bluetooth-Headphones-Earphones/dp/B08P5S3YDF/ref=sr_1_11?dchild=1&keywords=earphones&qid=1624238885&sr=8-11', 'https://www.amazon.com/VEATOOL-Wireless-Bluetooth-Headphones-Earphones/dp/B08P5S3YDF/ref=sr_1_11?dchild=1&keywords=earphones&qid=1624238885&sr=8-11', 'javascript:void(0)', 'https://www.amazon.com/VEATOOL-Wireless-Bluetooth-Headphones-Earphones/dp/B08P5S3YDF/ref=sr_1_11?dchild=1&keywords=earphones&qid=1624238885&sr=8-11#customerReviews', 'https://www.amazon.com/VEATOOL-Wireless-Bluetooth-Headphones-Earphones/dp/B08P5S3YDF/ref=sr_1_11?dchild=1&keywords=earphones&qid=1624238885&sr=8-11', 'https://www.amazon.com/gp/offer-listing/B08P5S3YDF/ref=sr_1_11_olp?keywords=earphones&qid=1624238885&sr=8-11&dchild=1', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A07389723VVPPEOX1VSH&url=%2FEarphones-Headphones-Microphone-Earbuds-Smartphones%2Fdp%2FB08B5F336L%2Fref%3Dsr_1_12_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26smid%3DAIAK2WCBRFSU%26sr%3D8-12-spons%26psc%3D1%26smid%3DAIAK2WCBRFSU&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A07389723VVPPEOX1VSH&url=%2FEarphones-Headphones-Microphone-Earbuds-Smartphones%2Fdp%2FB08B5F336L%2Fref%3Dsr_1_12_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26smid%3DAIAK2WCBRFSU%26sr%3D8-12-spons%26psc%3D1%26smid%3DAIAK2WCBRFSU&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'javascript:void(0)', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A07389723VVPPEOX1VSH&url=%2FEarphones-Headphones-Microphone-Earbuds-Smartphones%2Fdp%2FB08B5F336L%2Fref%3Dsr_1_12_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26smid%3DAIAK2WCBRFSU%26sr%3D8-12-spons%26psc%3D1%26smid%3DAIAK2WCBRFSU&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf#customerReviews', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A07389723VVPPEOX1VSH&url=%2FEarphones-Headphones-Microphone-Earbuds-Smartphones%2Fdp%2FB08B5F336L%2Fref%3Dsr_1_12_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26smid%3DAIAK2WCBRFSU%26sr%3D8-12-spons%26psc%3D1%26smid%3DAIAK2WCBRFSU&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'https://www.amazon.com/Sony-MDREX15AP-B-Black/dp/B00JG2WRUO/ref=sr_1_13?dchild=1&keywords=earphones&qid=1624238885&sr=8-13', 'https://www.amazon.com/Sony-MDREX15AP-B-Black/dp/B00JG2WRUO/ref=sr_1_13?dchild=1&keywords=earphones&qid=1624238885&sr=8-13', 'javascript:void(0)', 'https://www.amazon.com/Sony-MDREX15AP-B-Black/dp/B00JG2WRUO/ref=sr_1_13?dchild=1&keywords=earphones&qid=1624238885&sr=8-13#customerReviews', 'https://www.amazon.com/MIFA-Wireless-Bluetooth-Headphones-Earphones/dp/B08R8GBWQ1/ref=sr_1_14?dchild=1&keywords=earphones&qid=1624238885&sr=8-14', 'https://www.amazon.com/MIFA-Wireless-Bluetooth-Headphones-Earphones/dp/B08R8GBWQ1/ref=sr_1_14?dchild=1&keywords=earphones&qid=1624238885&sr=8-14', 'javascript:void(0)', 'https://www.amazon.com/MIFA-Wireless-Bluetooth-Headphones-Earphones/dp/B08R8GBWQ1/ref=sr_1_14?dchild=1&keywords=earphones&qid=1624238885&sr=8-14#customerReviews', 'https://www.amazon.com/MIFA-Wireless-Bluetooth-Headphones-Earphones/dp/B08R8GBWQ1/ref=sr_1_14?dchild=1&keywords=earphones&qid=1624238885&sr=8-14', 'https://www.amazon.com/Hntmao-Waterproof-Bluetooth-Headphones-Earphones/dp/B08ZRY2DYC/ref=sr_1_15?dchild=1&keywords=earphones&qid=1624238885&sr=8-15', 'https://www.amazon.com/Hntmao-Waterproof-Bluetooth-Headphones-Earphones/dp/B08ZRY2DYC/ref=sr_1_15?dchild=1&keywords=earphones&qid=1624238885&sr=8-15', 'javascript:void(0)', 'https://www.amazon.com/Hntmao-Waterproof-Bluetooth-Headphones-Earphones/dp/B08ZRY2DYC/ref=sr_1_15?dchild=1&keywords=earphones&qid=1624238885&sr=8-15#customerReviews', 'https://www.amazon.com/Hntmao-Waterproof-Bluetooth-Headphones-Earphones/dp/B08ZRY2DYC/ref=sr_1_15?dchild=1&keywords=earphones&qid=1624238885&sr=8-15', 'https://www.amazon.com/Beats-Flex-Wireless-Earphones-Built/dp/B08L6ZYW21/ref=sr_1_16?dchild=1&keywords=earphones&qid=1624238885&sr=8-16', 'https://www.amazon.com/Beats-Flex-Wireless-Earphones-Built/dp/B08L6ZYW21/ref=sr_1_16?dchild=1&keywords=earphones&qid=1624238885&sr=8-16', 'javascript:void(0)', 'https://www.amazon.com/Beats-Flex-Wireless-Earphones-Built/dp/B08L6ZYW21/ref=sr_1_16?dchild=1&keywords=earphones&qid=1624238885&sr=8-16#customerReviews', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A0785583XLBQNRAVBQ82&url=%2FHeadphones-Microphone-Compatible-Computers-Interface%2Fdp%2FB08MC6PLT4%2Fref%3Dsr_1_17_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-17-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A0785583XLBQNRAVBQ82&url=%2FHeadphones-Microphone-Compatible-Computers-Interface%2Fdp%2FB08MC6PLT4%2Fref%3Dsr_1_17_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-17-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'javascript:void(0)', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A0785583XLBQNRAVBQ82&url=%2FHeadphones-Microphone-Compatible-Computers-Interface%2Fdp%2FB08MC6PLT4%2Fref%3Dsr_1_17_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-17-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf#customerReviews', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A0785583XLBQNRAVBQ82&url=%2FHeadphones-Microphone-Compatible-Computers-Interface%2Fdp%2FB08MC6PLT4%2Fref%3Dsr_1_17_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-17-spons%26psc%3D1&qualifier=1624238885&id=7714708109019064&widgetName=sp_mtf', 'https://www.amazon.com/Certified-Pack-Apple-Headphones-Microphone-Compatible/dp/B0967GSHKL/ref=sr_1_18?dchild=1&keywords=earphones&qid=1624238885&sr=8-18', 'https://www.amazon.com/Certified-Pack-Apple-Headphones-Microphone-Compatible/dp/B0967GSHKL/ref=sr_1_18?dchild=1&keywords=earphones&qid=1624238885&sr=8-18', 'javascript:void(0)', 'https://www.amazon.com/Certified-Pack-Apple-Headphones-Microphone-Compatible/dp/B0967GSHKL/ref=sr_1_18?dchild=1&keywords=earphones&qid=1624238885&sr=8-18#customerReviews', 'https://www.amazon.com/Certified-Pack-Apple-Headphones-Microphone-Compatible/dp/B0967GSHKL/ref=sr_1_18?dchild=1&keywords=earphones&qid=1624238885&sr=8-18', 'https://www.amazon.com/Connector-Headphones-Earphones-Isolation-Compatible/dp/B089PYQQSQ/ref=sr_1_19?dchild=1&keywords=earphones&qid=1624238885&sr=8-19', 'https://www.amazon.com/Connector-Headphones-Earphones-Isolation-Compatible/dp/B089PYQQSQ/ref=sr_1_19?dchild=1&keywords=earphones&qid=1624238885&sr=8-19', 'javascript:void(0)', 'https://www.amazon.com/Connector-Headphones-Earphones-Isolation-Compatible/dp/B089PYQQSQ/ref=sr_1_19?dchild=1&keywords=earphones&qid=1624238885&sr=8-19#customerReviews', 'https://www.amazon.com/Connector-Headphones-Earphones-Isolation-Compatible/dp/B089PYQQSQ/ref=sr_1_19?dchild=1&keywords=earphones&qid=1624238885&sr=8-19', 'https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/ref=sr_1_20?dchild=1&keywords=earphones&qid=1624238885&sr=8-20', 'https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/ref=sr_1_20?dchild=1&keywords=earphones&qid=1624238885&sr=8-20', 'javascript:void(0)', 'https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/ref=sr_1_20?dchild=1&keywords=earphones&qid=1624238885&sr=8-20#customerReviews', 'https://www.amazon.com/Headphones-Microphone-Isolating-Earphones-Compatible/dp/B092VJVGZX/ref=sr_1_21?dchild=1&keywords=earphones&qid=1624238885&sr=8-21', 'https://www.amazon.com/Headphones-Microphone-Isolating-Earphones-Compatible/dp/B092VJVGZX/ref=sr_1_21?dchild=1&keywords=earphones&qid=1624238885&sr=8-21', 'javascript:void(0)', 'https://www.amazon.com/Headphones-Microphone-Isolating-Earphones-Compatible/dp/B092VJVGZX/ref=sr_1_21?dchild=1&keywords=earphones&qid=1624238885&sr=8-21#customerReviews', 'https://www.amazon.com/Headphones-Microphone-Isolating-Earphones-Compatible/dp/B092VJVGZX/ref=sr_1_21?dchild=1&keywords=earphones&qid=1624238885&sr=8-21', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_btf_aps_sr_pg1_1?ie=UTF8&adId=A08919421UZTG4Y5DWXXT&url=%2FHeadphone-Earphones-CBGGQ-Headphones-Microphone%2Fdp%2FB07XRXHHMP%2Fref%3Dsr_1_22_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-22-spons%26psc%3D1%26smid%3DA1SO1NT347NQHQ&qualifier=1624238885&id=7714708109019064&widgetName=sp_btf', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_btf_aps_sr_pg1_1?ie=UTF8&adId=A08919421UZTG4Y5DWXXT&url=%2FHeadphone-Earphones-CBGGQ-Headphones-Microphone%2Fdp%2FB07XRXHHMP%2Fref%3Dsr_1_22_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-22-spons%26psc%3D1%26smid%3DA1SO1NT347NQHQ&qualifier=1624238885&id=7714708109019064&widgetName=sp_btf', 'javascript:void(0)', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_btf_aps_sr_pg1_1?ie=UTF8&adId=A08919421UZTG4Y5DWXXT&url=%2FHeadphone-Earphones-CBGGQ-Headphones-Microphone%2Fdp%2FB07XRXHHMP%2Fref%3Dsr_1_22_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-22-spons%26psc%3D1%26smid%3DA1SO1NT347NQHQ&qualifier=1624238885&id=7714708109019064&widgetName=sp_btf#customerReviews', 'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_btf_aps_sr_pg1_1?ie=UTF8&adId=A08919421UZTG4Y5DWXXT&url=%2FHeadphone-Earphones-CBGGQ-Headphones-Microphone%2Fdp%2FB07XRXHHMP%2Fref%3Dsr_1_22_sspa%3Fdchild%3D1%26keywords%3Dearphones%26qid%3D1624238885%26sr%3D8-22-spons%26psc%3D1%26smid%3DA1SO1NT347NQHQ&qualifier=1624238885&id=7714708109019064&widgetName=sp_btf', 'https://www.amazon.com/s/?k=earbuds&ref=sugsr_0_10&pd_rd_w=GDgyg&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=f1a8650f-8951-463e-8eda-8121850943d8&pd_rd_wg=p9MTY&qid=1624238885', 'https://www.amazon.com/s/?k=earphones+bluetooth+wireless&ref=sugsr_3_8&pd_rd_w=GDgyg&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=f1a8650f-8951-463e-8eda-8121850943d8&pd_rd_wg=p9MTY&qid=1624238885', 'https://www.amazon.com/s/?k=earphones+with+microphone&ref=sugsr_1_10&pd_rd_w=GDgyg&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=f1a8650f-8951-463e-8eda-8121850943d8&pd_rd_wg=p9MTY&qid=1624238885', 'https://www.amazon.com/s/?k=earpods&ref=sugsr_4_5&pd_rd_w=GDgyg&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=f1a8650f-8951-463e-8eda-8121850943d8&pd_rd_wg=p9MTY&qid=1624238885', 'https://www.amazon.com/s/?k=headphones&ref=sugsr_2_9&pd_rd_w=GDgyg&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=f1a8650f-8951-463e-8eda-8121850943d8&pd_rd_wg=p9MTY&qid=1624238885', 'https://www.amazon.com/s/?k=earphones+for+iphone&ref=sugsr_5_4&pd_rd_w=GDgyg&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=f1a8650f-8951-463e-8eda-8121850943d8&pd_rd_wg=p9MTY&qid=1624238885', 'https://www.amazon.com/s?k=earphones&qid=1624238885&ref=sr_pg_1', 'https://www.amazon.com/s?k=earphones&page=2&qid=1624238885&ref=sr_pg_2', 'https://www.amazon.com/s?k=earphones&page=3&qid=1624238885&ref=sr_pg_3', 'https://www.amazon.com/s?k=earphones&page=2&qid=1624238885&ref=sr_pg_1', 'https://aax-us-east.amazon-adsystem.com/x/c/QvfIoNFf2bliMK1g8-ZIR-sAAAF6LC6NFgEAAAH2AVihO_0/https://www.amazon.com/stores/page/7CE86C9E-9BAF-4054-AB42-0FEA6F112993?store_ref=SB_A07480362U0J7Z9NW40RQ&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=4e6150363a2af3b9b8509ac2f83cf472&hsa_cr_id=2500675690801&lp_asins=B084X7Y51M,B0001FTVEK,B07RFNZYJZ&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd', 'https://aax-us-east.amazon-adsystem.com/x/c/QvfIoNFf2bliMK1g8-ZIR-sAAAF6LC6NFgEAAAH2AVihO_0/https://www.amazon.com/stores/page/7CE86C9E-9BAF-4054-AB42-0FEA6F112993?store_ref=SB_A07480362U0J7Z9NW40RQ&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=4e6150363a2af3b9b8509ac2f83cf472&hsa_cr_id=2500675690801&lp_asins=B084X7Y51M,B0001FTVEK,B07RFNZYJZ&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd', 'https://aax-us-east.amazon-adsystem.com/x/c/QvfIoNFf2bliMK1g8-ZIR-sAAAF6LC6NFgEAAAH2AVihO_0/https://www.amazon.com/stores/page/7CE86C9E-9BAF-4054-AB42-0FEA6F112993?store_ref=SB_A07480362U0J7Z9NW40RQ&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=4e6150363a2af3b9b8509ac2f83cf472&hsa_cr_id=2500675690801&lp_asins=B084X7Y51M,B0001FTVEK,B07RFNZYJZ&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd_bkgd', 'https://aax-us-east.amazon-adsystem.com/x/c/QmEUzRXWs8LndjFE56zJpDgAAAF6LC6NFgEAAAH2AahQvXo/https://www.amazon.com/stores/page/FC849B40-922B-4C85-8F0E-CF12C9E761E0?store_ref=SB_A0820333BHULKA6XE18X&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=1736571c2b90d1070adad18ce075f9ec&hsa_cr_id=2022660800401&lp_asins=B08RDGKT9Z,B08M95H1YY,B08GCMSZ74&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd', 'https://aax-us-east.amazon-adsystem.com/x/c/QmEUzRXWs8LndjFE56zJpDgAAAF6LC6NFgEAAAH2AahQvXo/https://www.amazon.com/stores/page/FC849B40-922B-4C85-8F0E-CF12C9E761E0?store_ref=SB_A0820333BHULKA6XE18X&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=1736571c2b90d1070adad18ce075f9ec&hsa_cr_id=2022660800401&lp_asins=B08RDGKT9Z,B08M95H1YY,B08GCMSZ74&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd', 'https://aax-us-east.amazon-adsystem.com/x/c/QmEUzRXWs8LndjFE56zJpDgAAAF6LC6NFgEAAAH2AahQvXo/https://www.amazon.com/stores/page/FC849B40-922B-4C85-8F0E-CF12C9E761E0?store_ref=SB_A0820333BHULKA6XE18X&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=1736571c2b90d1070adad18ce075f9ec&hsa_cr_id=2022660800401&lp_asins=B08RDGKT9Z,B08M95H1YY,B08GCMSZ74&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd_bkgd', 'https://aax-us-east.amazon-adsystem.com/x/c/QhynYB_LSMQDoSiyTwlF_VoAAAF6LC6NFgEAAAH2AfUfeI4/https://www.amazon.com/stores/page/04CB530B-7FDD-441D-B18C-05DC6E9D28A8?store_ref=SB_A0819317JIGN6WS9HH83&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=e350d5d458433f669eff18a3e18f399a&hsa_cr_id=9764176410701&lp_asins=B083J7BPD4,B08BJS1SNT,B083FQ7BYQ&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd', 'https://aax-us-east.amazon-adsystem.com/x/c/QhynYB_LSMQDoSiyTwlF_VoAAAF6LC6NFgEAAAH2AfUfeI4/https://www.amazon.com/stores/page/04CB530B-7FDD-441D-B18C-05DC6E9D28A8?store_ref=SB_A0819317JIGN6WS9HH83&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=e350d5d458433f669eff18a3e18f399a&hsa_cr_id=9764176410701&lp_asins=B083J7BPD4,B08BJS1SNT,B083FQ7BYQ&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd', 'https://aax-us-east.amazon-adsystem.com/x/c/QhynYB_LSMQDoSiyTwlF_VoAAAF6LC6NFgEAAAH2AfUfeI4/https://www.amazon.com/stores/page/04CB530B-7FDD-441D-B18C-05DC6E9D28A8?store_ref=SB_A0819317JIGN6WS9HH83&pd_rd_w=oQ1Iz&pf_rd_p=eec71719-2cb3-403b-a8de-e6266852cdb6&pd_rd_wg=JSY77&pf_rd_r=N9411CP5TYYQ3W9JDBB4&pd_rd_r=6cdcd27e-e4be-4f1b-b592-970f2713f21f&aaxitk=e350d5d458433f669eff18a3e18f399a&hsa_cr_id=9764176410701&lp_asins=B083J7BPD4,B08BJS1SNT,B083FQ7BYQ&lp_query=earphones&lp_slot=desktop-hsa-3psl&ref_=sbx_be_s_3psl_mbd_bkgd', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=468556', 'https://www.amazon.com/gp/help/customer/contact-us', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#s-skipLinkTargetForFilterOptions', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#s-skipLinkTargetForMainSearchResults', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541&dc&qid=1624238885&rnid=2941120011&ref=sr_nr_n_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cn%3A12097478011&dc&qid=1624238885&rnid=2941120011&ref=sr_nr_n_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cn%3A12097479011&dc&qid=1624238885&rnid=2941120011&ref=sr_nr_n_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cn%3A12097480011&dc&qid=1624238885&rnid=2941120011&ref=sr_nr_n_4', 'https://www.amazon.com/s?k=earphones&i=electronics&dc&qid=1624238885&ref=sr_nr_i_5', 'https://www.amazon.com/s?k=earphones&i=mobile&dc&qid=1624238885&ref=sr_nr_i_6', 'https://www.amazon.com/s?k=earphones&i=videogames&dc&qid=1624238885&ref=sr_nr_i_7', 'https://www.amazon.com/s?k=earphones&i=sporting&dc&qid=1624238885&ref=sr_nr_i_8', 'https://www.amazon.com/s?k=earphones&i=fashion&dc&qid=1624238885&ref=sr_nr_i_9', 'https://www.amazon.com/s?k=earphones&i=office-products&dc&qid=1624238885&ref=sr_nr_i_10', 'https://www.amazon.com/s?k=earphones&i=garden&dc&qid=1624238885&ref=sr_nr_i_11', 'https://www.amazon.com/s?k=earphones&i=industrial&dc&qid=1624238885&ref=sr_nr_i_12', 'https://www.amazon.com/s?k=earphones&i=stripbooks&dc&qid=1624238885&ref=sr_nr_i_13', 'https://www.amazon.com/s?k=earphones&i=mi&dc&qid=1624238885&ref=sr_nr_i_14', 'https://www.amazon.com/s?k=earphones&i=tools&dc&qid=1624238885&ref=sr_nr_i_15', 'https://www.amazon.com/s?k=earphones&i=automotive&dc&qid=1624238885&ref=sr_nr_i_16', 'https://www.amazon.com/s?k=earphones&i=misc&dc&qid=1624238885&ref=sr_nr_i_17', 'https://www.amazon.com/s?k=earphones&i=beauty&dc&qid=1624238885&ref=sr_nr_i_18', 'https://www.amazon.com/s?k=earphones&i=toys-and-games&dc&qid=1624238885&ref=sr_nr_i_19', 'https://www.amazon.com/s?k=earphones&i=hpc&dc&qid=1624238885&ref=sr_nr_i_20', 'https://www.amazon.com/s?k=earphones&i=arts-crafts&dc&qid=1624238885&ref=sr_nr_i_21', 'https://www.amazon.com/s?k=earphones&i=baby-products&dc&qid=1624238885&ref=sr_nr_i_22', 'https://www.amazon.com/s?k=earphones&i=lawngarden&dc&qid=1624238885&ref=sr_nr_i_23', 'https://www.amazon.com/s?k=earphones&i=appliances&dc&qid=1624238885&ref=sr_nr_i_24', 'https://www.amazon.com/s?k=earphones&i=pets&dc&qid=1624238885&ref=sr_nr_i_25', 'https://www.amazon.com/s?k=earphones&i=dvd&dc&qid=1624238885&ref=sr_nr_i_26', 'https://www.amazon.com/s?k=earphones&i=digital-music&dc&qid=1624238885&ref=sr_nr_i_27', 'https://www.amazon.com/s?k=earphones&i=popular&dc&qid=1624238885&ref=sr_nr_i_28', 'https://www.amazon.com/s?k=earphones&i=handmade&dc&qid=1624238885&ref=sr_nr_i_29', 'https://www.amazon.com/s?k=earphones&i=grocery&dc&qid=1624238885&ref=sr_nr_i_30', 'https://www.amazon.com/s?k=earphones&i=collectibles&dc&qid=1624238885&ref=sr_nr_i_31', 'https://www.amazon.com/s?k=earphones&i=kindle-accessories&dc&qid=1624238885&ref=sr_nr_i_32', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_72%3A1248879011&dc&qid=1624238885&rnid=1248877011&ref=sr_nr_p_72_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_72%3A1248880011&dc&qid=1624238885&rnid=1248877011&ref=sr_nr_p_72_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_72%3A1248881011&dc&qid=1624238885&rnid=1248877011&ref=sr_nr_p_72_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_72%3A1248882011&dc&qid=1624238885&rnid=1248877011&ref=sr_nr_p_72_4', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Asephia&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ATOZO&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AApple&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3APanasonic&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_4', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASony&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_5', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AJLAB&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_6', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASymphonized&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_7', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ABeats&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_8', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AVEATOOL&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_9', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ALETSCOM&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_10', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AAmoner&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_11', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ALudos&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_12', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AYNR&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_13', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Aocciam&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_14', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AVOGEK&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_15', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AZVOLTZ&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_16', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASoundcore&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_17', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AAxloie&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_18', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ABose&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_19', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AAUKEY&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_20', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3A1MORE&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_21', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AMIFA&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_22', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AM+MOVONE&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_23', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AOtium&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_24', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AVPB&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_25', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASanluba&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_26', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Acowin&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_27', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AENACFIRE&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_28', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AHolyHigh&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_29', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Avankyo&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_30', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ALASUNEY&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_31', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AMuGo&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_32', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASkullcandy&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_33', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AMaeline&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_34', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AFiiO&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_35', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ATribit&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_36', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASAMSUNG&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_37', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ATANGMAI&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_38', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3APurity&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_39', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Apendali&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_40', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AAvantree&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_41', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AHadisala&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_42', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AL+LINPA+WORLD&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_43', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ABEARTWO&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_44', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AJabra&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_45', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Akurdene&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_46', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AHedGear&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_47', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3ASoundPEATS&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_48', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3AFinance+Plan&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_49', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_89%3Aslitinto&dc&qid=1624238885&rnid=2528832011&ref=sr_nr_p_89_50', 'javascript:void(0)', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_36%3A1253503011&dc&qid=1624238885&rnid=386442011&ref=sr_nr_p_36_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_36%3A1253504011&dc&qid=1624238885&rnid=386442011&ref=sr_nr_p_36_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_36%3A1253505011&dc&qid=1624238885&rnid=386442011&ref=sr_nr_p_36_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_36%3A1253506011&dc&qid=1624238885&rnid=386442011&ref=sr_nr_p_36_4', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_36%3A1253507011&dc&qid=1624238885&rnid=386442011&ref=sr_nr_p_36_5', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_five_browse-bin%3A17751345011&dc&qid=1624238885&rnid=17751344011&ref=sr_nr_p_n_feature_five_browse-bin_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_five_browse-bin%3A17751346011&dc&qid=1624238885&rnid=17751344011&ref=sr_nr_p_n_feature_five_browse-bin_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972982011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972988011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972996011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972984011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_4', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972981011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_5', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972994011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_6', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972992011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_7', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972991011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_8', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972997011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_9', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972989011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_10', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972987011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_11', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972983011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_12', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972993011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_13', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972986011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_14', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972995011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_15', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972990011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_16', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_twenty_browse-bin%3A2972985011&dc&qid=1624238885&rnid=2972980011&ref=sr_nr_p_n_feature_twenty_browse-bin_17', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A6131842011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097487011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097488011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A2266981011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_4', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097489011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_5', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A2266980011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_6', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097493011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_7', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A12097494011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_8', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A6131843011&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_9', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_two_browse-bin%3A509316&dc&qid=1624238885&rnid=2266979011&ref=sr_nr_p_n_feature_two_browse-bin_10', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_four_browse-bin%3A12097501011&dc&qid=1624238885&rnid=12097500011&ref=sr_nr_p_n_feature_four_browse-bin_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_four_browse-bin%3A12097502011&dc&qid=1624238885&rnid=12097500011&ref=sr_nr_p_n_feature_four_browse-bin_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_four_browse-bin%3A12097503011&dc&qid=1624238885&rnid=12097500011&ref=sr_nr_p_n_feature_four_browse-bin_3', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_four_browse-bin%3A12097504011&dc&qid=1624238885&rnid=12097500011&ref=sr_nr_p_n_feature_four_browse-bin_4', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_four_browse-bin%3A12097505011&dc&qid=1624238885&rnid=12097500011&ref=sr_nr_p_n_feature_four_browse-bin_5', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_three_browse-bin%3A12097498011&dc&qid=1624238885&rnid=12097495011&ref=sr_nr_p_n_feature_three_browse-bin_2', 'https://www.amazon.com/s?k=earphones&rh=n%3A172541%2Cp_n_feature_three_browse-bin%3A12097499011&dc&qid=1624238885&rnid=12097495011&ref=sr_nr_p_n_feature_three_browse-bin_3', 'https://www.amazon.com/s?k=earphones&rh=p_n_amazon_certified%3A16741513011&dc&qid=1624238885&rnid=16741512011&ref=sr_nr_p_n_amazon_certified_1', 'https://www.amazon.com/s?k=earphones&rh=p_n_feature_forty-seven_browse-bin%3A21180942011&dc&qid=1624238885&rnid=21180941011&ref=sr_nr_p_n_feature_forty-seven_browse-bin_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_n_is_ffp%3A7252855011&dc&qid=1624238885&rnid=7252854011&ref=sr_nr_p_n_is_ffp_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_n_date%3A1249033011&dc&qid=1624238885&rnid=1249031011&ref=sr_nr_p_n_date_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_n_special_merchandising_browse-bin%3A544495011&dc&qid=1624238885&rnid=544494011&ref=sr_nr_p_n_special_merchandising_browse-bin_1', 'https://www.amazon.com/s?k=earphones&rh=p_n_global_store_origin_marketplace%3A16354393011&dc&qid=1624238885&rnid=16354392011&ref=sr_nr_p_n_global_store_origin_marketplace_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_n_condition-type%3A2224371011&dc&qid=1624238885&rnid=2224369011&ref=sr_nr_p_n_condition-type_1', 'https://www.amazon.com/s?k=earphones&rh=n%3A172282%2Cp_n_condition-type%3A2224373011&dc&qid=1624238885&rnid=2224369011&ref=sr_nr_p_n_condition-type_2', 'https://www.amazon.com/s?k=earphones&rh=p_n_availability%3A2661601011&dc&qid=1624238885&rnid=2661599011&ref=sr_nr_p_n_availability_2', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#', 'https://www.amazon.com/gp/yourstore/pym/ref=pd_pyml_rhf', 'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss#nav-top', 'https://www.amazon.jobs/', 'https://blog.aboutamazon.com/?utm_source=gateway&utm_medium=footer', 'https://www.aboutamazon.com/?utm_source=gateway&utm_medium=footer', 'https://www.amazon.com/ir', 'https://www.amazon.com/gp/browse.html?node=2102313011&ref_=footer_devices', 'https://services.amazon.com/sell.html?ld=AZFSSOA&ref_=footer_soa', 'https://services.amazon.com/amazon-business.html?ld=usb2bunifooter&ref_=footer_b2b', 'https://developer.amazon.com/', 'https://affiliate-program.amazon.com/', 'https://advertising.amazon.com/?ref=ext_amzn_ftr', 'https://www.amazon.com/gp/seller-account/mm-summary-page.html?ld=AZFooterSelfPublish&topic=200260520&ref_=footer_publishing', 'http://go.thehub-amazon.com/amazon-hub-locker', 'https://www.amazon.com/b/?node=18190131011&ld=AZUSSOA-seemore&ref_=footer_seemore', 'https://www.amazon.com/dp/B07984JN3L?plattr=ACOMFO&ie=UTF-8', 'https://www.amazon.com/gp/browse.html?node=16218619011&ref_=footer_swp', 'https://www.amazon.com/gp/browse.html?node=10232440011&ref_=footer_reload_us', 'https://www.amazon.com/gp/browse.html?node=388305011&ref_=footer_tfx', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GDFU3JS5AL6SYHRD&ref_=footer_covid', 'https://www.amazon.com/gp/css/homepage.html?ref_=footer_ya', 'https://www.amazon.com/gp/css/order-history?ref_=footer_yo', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=468520&ref_=footer_shiprates', 'https://www.amazon.com/gp/css/returns/homepage.html?ref_=footer_hy_f_4', 'https://www.amazon.com/gp/digital/fiona/manage?ref_=footer_myk', 'https://www.amazon.com/gp/BIT/ref=footer_bit_v2_us_A0029?bitCampaignCode=A0029', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=508510&ref_=footer_gw_m_b_he', 'https://www.amazon.com/?ref_=footer_logo', 'https://www.amazon.com/gp/customer-preferences/select-language/ref=footer_lang?ie=UTF8&preferencesReturnUrl=%2Fs%3Fk%3Dearphones%26ref%3Dnb_sb_noss', 'https://www.amazon.com/gp/customer-preferences/select-currency?ie=UTF8&ref_=footer_cop&preferencesReturnUrl=%2Fs%3Fk%3Dearphones%26ref%3Dnb_sb_nosss%2Fref%3Dnb_sb_noss', 'https://www.amazon.com/gp/navigation-country/select-country/ref=footer_icp_cp?ie=UTF8&preferencesReturnUrl=%2Fs%3Fk%3Dearphones%26ref%3Dnb_sb_noss', 'https://music.amazon.com/?ref=dm_aff_amz_com', 'https://advertising.amazon.com/?ref=footer_advtsing_amzn_com', 'https://www.amazon.com/gp/browse.html?node=15547130011&ref_=_us_footer_drive', 'https://www.6pm.com/', 'https://www.abebooks.com/', 'https://www.acx.com/', 'https://www.alexa.com/', 'https://sell.amazon.com/?ld=AZUSSOA-footer-aff&ref_=footer_sell', 'https://www.amazon.com/business?ref_=footer_retail_b2b', 'https://www.amazon.com/gp/browse.html?node=230659011&ref_=footer_amazonglobal', 'https://www.amazon.com/services?ref_=footer_services', 'https://ignite.amazon.com/?ref=amazon_footer_ignite', 'https://aws.amazon.com/what-is-cloud-computing/?sc_channel=EL&sc_campaign=amazonfooter', 'https://www.audible.com/', 'https://www.bookdepository.com/', 'https://www.boxofficemojo.com/?ref_=amzn_nav_ftr', 'https://www.comixology.com/', 'https://www.dpreview.com/', 'https://www.eastdane.com/welcome', 'https://www.fabric.com/', 'https://www.goodreads.com/', 'https://www.imdb.com/', 'https://pro.imdb.com/?ref_=amzn_nav_ftr', 'https://kdp.amazon.com/', 'https://videodirect.amazon.com/home/landing', 'https://www.shopbop.com/welcome', 'https://www.woot.com/', 'https://www.zappos.com/', 'https://ring.com/', 'https://eero.com/', 'https://blinkforhome.com/?ref=nav_footer', 'https://shop.ring.com/pages/neighbors-app', 'https://www.amazon.com/gp/browse.html?node=14498690011&ref_=amzn_nav_ftr_swa', 'https://www.pillpack.com/', 'https://www.amazon.com/amazonsecondchance?ref_=footer_asc', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou', 'https://www.amazon.com/gp/help/customer/display.html?nodeId=468496&ref_=footer_privacy', 'https://www.amazon.com/interestbasedads/ref=footer_iba']\n"
     ]
    }
   ],
   "source": [
    "all_link = []\n",
    "sel_all = driver.find_elements_by_xpath('//a[@href]')\n",
    "for i in sel_all:\n",
    "    all_link.append(i.get_attribute('href'))\n",
    "print(all_link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "dict_doc = {'text' : all_link}\n",
    "doc = pd.DataFrame(dict_doc)\n",
    "doc.to_csv(\"아마존링크.csv\", index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.amazon.com/Headphones-Bluetooth-Reduction-Microphone-Compatible/dp/B095RHGZKB/ref=sr_1_1_sspa?dchild=1&keywords=earphones&qid=1624238885&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWjA2NEJXMUZKNk00JmVuY3J5cHRlZElkPUEwMzk2MDY2N1YwRUkySDUyNVYzJmVuY3J5cHRlZEFkSWQ9QTA4NzAxOTQxMjlUS0ZFRFo4TUFPJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "sel_review=driver.find_element_by_xpath('//*[@id=\"acrCustomerReviewText\"]')\n",
    "sel_review.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "sel_all_review=driver.find_element_by_xpath('//*[@id=\"reviews-medley-footer\"]/div[2]/a')\n",
    "sel_all_review.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['We made hot chocolate bombs. Love the size and how the mold peels right off the chocolate without breaking it! Kids had a blast! Would recommend!', \"Ok I was skeptical and watched so many videos to not mess up the process. Turns out that I believe what's important is the quality of chocolate you use. Anything that stays solid at room temperature and is semi gourmet is perfect! Candy bars not so much as they melt while handling. Stuffed full with baby marshmallows and hot chocolate nesquick mix and some brown sugar. My boys loved the rich bombs made in milk. The balls are large and perfect size to fit in a big mug. I stored ours in the fridge.\\nWe also painted on two layers of chocolate and cooled in the fridge after each layer. Areas to be careful with are the bomb edges that seal as well as the bottom center, i ended up with a couple holes. No harm done still tasty just not pretty. Yes i recommend it and yes i would buy it again.\", 'I love how easy these are to use!! Great for beginners!!', 'These were so easy to use. Easy to clean as well. The chocolate popped right out once set. I think this is a great price and value. My first time making hot cocoa bombs was a success because of these molds. There are so many to choose from on Amazon but I think I made the right choice for sure!', 'The mold was the perfect size for a hot chocolate bomb! I read so many reviews before purchasing trying to get something that would be the right size, delivered quickly, & was easy to use. This mold was all of the above. As some mentioned, it is thin, buy that allows for easy removal of the molded item. It does also make it a little flattened on the ends because of that, so we used a cookie sheet underneath to help as it was so flexible and also put some bunched up parchment paper underneath to help take the pressure off of it sitting on the flat surface and it worked great. Kind of a pain to have to do that, but if the mold was harder it would make getting the stuff out of the molds harder. I am very happy with these molds and would purchase them again.', 'This product shipped fast and arrived on time. Good quality and makes an over 2\" hot cocoa bomb.\\nVery happy with this purchase. I bought 2 sets of 3 !! Easy to clean, easy to use.', 'Too flimsy, received a refund. A $10 gift card is offered for a five star review!', \"Great product! Worked well! Update The product works fine...nothing extraordinary, but I only wrote this review because they promised a Amazon gift card but never delivered on it...so I'm giving it 1 star because they lied and didn't fulfill their promise. That is all.\", 'First time making chocolate bombs and while the first one didn’t turn out great because my hands were too warm, the silicone molds made it very easy to remove! These spheres are 2.5 inches in diameter and are the perfect size for chocolate bombs! Also very easy to wash - just put them in the dishwasher! I didn’t have any silicone smell after I put it in the dishwasher as soon as I got it.', 'Unlike other seller which never delivered, after 2 weeks we ordered from them. Super fast delivery even during Christmas! The mold worked great for the cocoa bomb even my 8 year old was able to make them. Very happy!']\n"
     ]
    }
   ],
   "source": [
    "all_reviews=[]\n",
    "sel_take_reviews=driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]/div[4]/span')\n",
    "for i in sel_take_reviews:\n",
    "    all_reviews.append(i.text)\n",
    "print(all_reviews)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>review</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>We made hot chocolate bombs. Love the size and...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ok I was skeptical and watched so many videos ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I love how easy these are to use!! Great for b...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>These were so easy to use. Easy to clean as we...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>The mold was the perfect size for a hot chocol...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>This product shipped fast and arrived on time....</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Too flimsy, received a refund. A $10 gift card...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Great product! Worked well! Update The product...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>First time making chocolate bombs and while th...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Unlike other seller which never delivered, aft...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              review\n",
       "0  We made hot chocolate bombs. Love the size and...\n",
       "1  Ok I was skeptical and watched so many videos ...\n",
       "2  I love how easy these are to use!! Great for b...\n",
       "3  These were so easy to use. Easy to clean as we...\n",
       "4  The mold was the perfect size for a hot chocol...\n",
       "5  This product shipped fast and arrived on time....\n",
       "6  Too flimsy, received a refund. A $10 gift card...\n",
       "7  Great product! Worked well! Update The product...\n",
       "8  First time making chocolate bombs and while th...\n",
       "9  Unlike other seller which never delivered, aft..."
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dat_r = {'review' : all_reviews}\n",
    "dat = pd.DataFrame(dat_r)\n",
    "dat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat.to_csv('review.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.amazon.com/Headphones-Bluetooth-Reduction-Microphone-Compatible/product-reviews/B095RHGZKB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "sel_next_page = driver.find_element_by_xpath('//*[@id=\"cm_cr-pagination_bar\"]/ul/li[2]/a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We made hot chocolate bombs. Love the size and how the mold peels right off the chocolate without breaking it! Kids had a blast! Would recommend!\n",
      "Ok I was skeptical and watched so many videos to not mess up the process. Turns out that I believe what's important is the quality of chocolate you use. Anything that stays solid at room temperature and is semi gourmet is perfect! Candy bars not so much as they melt while handling. Stuffed full with baby marshmallows and hot chocolate nesquick mix and some brown sugar. My boys loved the rich bombs made in milk. The balls are large and perfect size to fit in a big mug. I stored ours in the fridge.\n",
      "We also painted on two layers of chocolate and cooled in the fridge after each layer. Areas to be careful with are the bomb edges that seal as well as the bottom center, i ended up with a couple holes. No harm done still tasty just not pretty. Yes i recommend it and yes i would buy it again.\n",
      "I love how easy these are to use!! Great for beginners!!\n",
      "These were so easy to use. Easy to clean as well. The chocolate popped right out once set. I think this is a great price and value. My first time making hot cocoa bombs was a success because of these molds. There are so many to choose from on Amazon but I think I made the right choice for sure!\n",
      "The mold was the perfect size for a hot chocolate bomb! I read so many reviews before purchasing trying to get something that would be the right size, delivered quickly, & was easy to use. This mold was all of the above. As some mentioned, it is thin, buy that allows for easy removal of the molded item. It does also make it a little flattened on the ends because of that, so we used a cookie sheet underneath to help as it was so flexible and also put some bunched up parchment paper underneath to help take the pressure off of it sitting on the flat surface and it worked great. Kind of a pain to have to do that, but if the mold was harder it would make getting the stuff out of the molds harder. I am very happy with these molds and would purchase them again.\n",
      "This product shipped fast and arrived on time. Good quality and makes an over 2\" hot cocoa bomb.\n",
      "Very happy with this purchase. I bought 2 sets of 3 !! Easy to clean, easy to use.\n",
      "Too flimsy, received a refund. A $10 gift card is offered for a five star review!\n",
      "Great product! Worked well! Update The product works fine...nothing extraordinary, but I only wrote this review because they promised a Amazon gift card but never delivered on it...so I'm giving it 1 star because they lied and didn't fulfill their promise. That is all.\n",
      "First time making chocolate bombs and while the first one didn’t turn out great because my hands were too warm, the silicone molds made it very easy to remove! These spheres are 2.5 inches in diameter and are the perfect size for chocolate bombs! Also very easy to wash - just put them in the dishwasher! I didn’t have any silicone smell after I put it in the dishwasher as soon as I got it.\n",
      "Unlike other seller which never delivered, after 2 weeks we ordered from them. Super fast delivery even during Christmas! The mold worked great for the cocoa bomb even my 8 year old was able to make them. Very happy!\n",
      "I was worried that these were going to be too small. In fact, they are a perfect size. With COVID to worry I used to use bigger ones and we used to share the dessert. Now, these are a perfect size. Not too big you need to share, not too small to stay hungry.\n",
      "Good quality too, Thanks!\n",
      "Delivered quickly, got them less than 3 days after I ordered them. They we're on sale and I love that they came with 3 mold trays. I got these specifically to make Hot Cocoa Bombs, they seem like great quality but also thin enough that it should be easy to pop them out of the molds without breaking.\n",
      "Just made my first cocoa bomb as a trial run.\n",
      "So easy and fun!!!! Very pleased with the size 6 Large spheres, Silicone baking molds.\n",
      "Like I reviewed earlier before trying, wish the company had included a recipe but found one on line.\n",
      "I'll need to refine my next cocoa bombs before I give away--but excited to do them for my grandkids.\n",
      "we love it!!! they work so well!! here is A picture of the mold with the finished product, a homemade hot cocoa bomb!!\n",
      "I love these molds. I was a little hesitant ordering them because I had ordered similar ones before that were too small. These are perfect and easy to use. They were big enough to add a packet of hot chocolate and marshmallows. I am very please with the results. :D\n",
      "I bought these to make hot cocoa balls for Valentine's Day. My teenage daughter and friend were able to make 30 of them in an hour! They were easy to use, especially the popping out part, and they clean up really well! Will be using these for many more holidays.\n",
      "Your browser does not support HTML5 video.\n",
      " I’m in love with the product look very good in shape materials look flexible when I’m done doing my bombshell I will make sure to put up with you but I think it will be a victory is my first time making them then I hope everything go well\n",
      "I got this as a gift for my 12 year old daughter who wantwd to learn to make hot cocoa bombs. We are still perfecting the method, but the chocolate came out easily and was easy to clean.\n",
      "Great customer service and product. This company did a great job responding to my emails and making the problem I had right! How many companies do that? This mold is easy to use and easy to clean- perfect for my hot chocolate bombs!\n",
      "These worked great for hot cocoa bombs! I had a lot of fun with my son making and yummy treats. They were a good size for an 8-10oz of liquid for your cocoa. Easy to pop out, even my 5 year old could do it without help. Very easy to clean too.\n",
      "I just recently started using silicone molds to make snacks for the family but was in need of something bigger. These molds were just what I was looking for and they hold up great.\n",
      "As a first timer making Hot Chocolate Bombs,\n",
      "these molds made it simple to do.\n",
      "They do make a big bomb so be ready with big cups! My Grandkids loved them!\n",
      "These chocolate bombs were of poor quality. They are so thin that they will not hold up to anything, including the chocolate for which they were intended. The $10 Amazon gift certificate offered for giving this company a 5/5 now explains all the great ratings. I am sorry I did not return them as they are useless.\n",
      "I purchase these molds to make hot chocolate bombs. I feel the size of them was too big & cause the hot chocolate to be too sweet. Also, the material they are made of is \"sticky\" on the outside & everything attaches to it.\n",
      "A bit of an odor when I first removed it from the packaging, but a quick wash was all it needed. This mold was exactly what I was looking for to make hot chocolate bombs.\n",
      "Love these! I plan on making hot cocoa bombs for Christmas so I’m excited to have these on hand. Super easy to clean and store. Thank you\n",
      "Super soft and flexible, no smell when the delivery came but I boiled them anyway. Large size to fill a coffee cup and fill with surprises. Looks great for jello too\n",
      "These silicone molds were easy to clean and easy to use. My chocolate separated well from them. However, there is not much sturdiness to the molds and so the domes did not have the perfect sphere shape.\n",
      "Will try to make the chocolate bomb\n",
      "Love the size and how easy it was to remove the hot chocolate bombs.\n",
      "Easy to wash, size was perfect and arrived a day early.\n",
      "Measurements matched what was listed.\n",
      "These were very easy to use. I just put in my melted chocolate in molds, put in fridge and they formed nicely and came out of the mold easily. They were also easy to clean.\n",
      "I have only used these for chocolate and they worked really well. Nice to throw them in the dishwasher. Would recommend.\n",
      "The size is what we’re were seeking for making hot chocolate bombs.\n",
      "The purple one in the photo is a different product that we bought, but they were to small to get all the marshmallows and cocoa mix.\n",
      "This product seems more like that right size.\n",
      "I bought these to make hot cocoa bombs and they worked very well! I need up cutting a few off as singles as I found them a little easier to work with that way but since it came in a 3 pack I still have 2 whole sheets. The cocoa bombshell turned out well and I imagine I can make all sorts of other items with these as well!\n",
      "We love these, kids and I have so much fun making the bombs and without mess or without breaking the half shapes. It comes out easy\n",
      "Great product. Used to make hot chocolate balls. The chocolate peeled off effortlessly after I put it in the freezer.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exactly as advertised..perfect for making coffee bombs..easy to clean, chocolate comes out easy..highly recommend\n",
      "I love these molds! Since the cocoa bomb craze I have been making them like crazy! This was a batch I made for my friends and their kids. I’m the cool aunt ;) FYI! And these molds were so easy to work with!\n",
      "We made coca bombs. These worked perfectly! I loved that they just push right out because they are so pliable.\n",
      "These hot chocolate bombs were so much fun to make with these molds. This was our first try at making them so I'm sure we'll get better with time. Mold were easy to clean and the chocolate came right out of the mold with no issues.\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,5):\n",
    "    url = 'https://www.amazon.com/Headphones-Bluetooth-Reduction-Microphone-Compatible/product-reviews/B095RHGZKB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)\n",
    "    driver.get(url)\n",
    "    sel_take_reviews=driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]/div[4]/span')\n",
    "    for i in sel_take_reviews:\n",
    "        print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os, warnings\n",
    "import re\n",
    "warnings.filterwarnings(action='ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome('chromedriver')\n",
    "## https://www.amazon.com/\n",
    "url = 'https://www.amazon.com/I-Love-You-Through/dp/0439673631/ref=pd_bkstr_rtpb_11?_encoding=UTF8&pd_rd_i=0439673631&pd_rd_r=b6408368-b4ad-4216-a355-4a9b5d3783ed&pd_rd_w=ctM06&pd_rd_wg=IqFxz&pf_rd_p=bde336d5-3a2a-4b7b-8e18-de1f4aaea610&pf_rd_r=65N1HJRRQHTWVKNBT9W6&psc=1&refRID=2XWPSHYF7973Q8W8T00B'\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "sel_review = driver.find_element_by_xpath('//*[@id=\"cr-pagination-footer-0\"]/a')\n",
    "sel_review.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "page = driver.page_source\n",
    "soup = BeautifulSoup(page, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Amazon Customer', 'Noha Anous', '2B4Elise', 'Amazon Customer', 'R. P.', 'Sparky127', 'Amazon Customer', 'CK', 'Anne', 'Renata']\n",
      "['5', '4', '2', '5', '5', '4', '5', '5', '5', '3']\n",
      "['September 7, 2020', 'February 8, 2021', 'March 12, 2020', 'September 25, 2016', 'July 23, 2018', 'March 16, 2012', 'December 18, 2019', 'August 10, 2016', 'December 31, 2020', 'January 14, 2021']\n",
      "[\"My friend told me this is a great bonding book that builds healthy attachement. She reccomended it for my 4 year old. I am not sure if there are 2 version but this is definetly not for his age. It is a beautiful cute lovely book. Love the messages & cute pictures. The pages are really nice and sturdy. comfortable cover. BUT its dissapointing cuz it's a one liner per page and he doesnt want me to read this one. I believe this is the perfect book to start reading when baby is a few months and then maybe if you read it so many times then by 4 a child will still love it because it is familiar, there are many bonding moments/memories associated with the book. I wish they had a version for older kids. I didnt return it cuz its a good quality book and it was a very good price. and I am still hoping my son will start enjoying it because the message is so great and so important. I doubt it though. This is really a 5 star book but for me its a 2-3 stars cuz just doesnt work for me.\", 'My son loves the book. I understand it’s about opposites, but I find the phrases ‘I love your top side ‘ and ‘I love your bottom side’ really strange. If my son repeats these phrases infront of any stranger, they would say why is this kid creepy!Otherwise, the book is nice with nice pictures and good material that my son can open the book and turn pages on his own. My son is 2.5 years.', \"I get that any book for a baby should be simple, but this one is a bit too much so.  There are other books (I Love You Because You're You) that communicate unconditional love, but in a rhythmic way that's fun to read to a baby.  On the plus side, the pictures are clear and simple, and I think some infants might like that.  Still, I'm a bit puzzled by all the 5 star ratings.\", \"What an adorable book!So many children's books have terrible story lines or messages in them, but definitely not the case with this book. It's a very simple book with no story, just about how you love (and always will love) every part and aspect of your baby. It can teach kids some body parts (like fingers, toes, ears, nose, hair, eyes), too. It rhymes, too.The only negative is, for a board book, the pages aren't very sturdy. The pages are maybe a third or half the thickness of other board books we own. Hopefully it'll hold up, because I am sure we will be reading this book frequently!\", 'Absolutely beautify book to read to your child.  The premise is so touching and our baby just loves this book.  We have been reading it everyday since the day he was born.', \"We absolutely love this book.It's been our son's favorite since he was about 9 months old.  The pictures are beautiful, colorful, and simple.  Not boring, not crowded, just what it should be.  The text is sweet and simple, the rhymes are thoughtful and not dumb (you know those books!), and the sentences are short enough to hold a baby's attention so we have time to get all the words out before he turns the page.The one downside is that this book is really cheaply made.  The cover is nice and padded, but the pages are cheap.  The pages are thinner than other board book pages, but the bigger problem is the actual surface of the pages.  Our son - an impressive drooler and finger-sucker - loves to turn the pages himself with his drool-y fingers and sometimes kiss the pages too.  What I didn't learn until too late is that you can't do that with this book.  For our other board books, you can get some drool on them and it just makes the pages stick together a little bit but that's it.  For this book, drool made the pages stick together so much that when you separated them later, the paper tore.  (See my pics in the photo gallery for examples)  I'm thinking that we can't be the only parents with a drooly baby, right??Quality notwithstanding, this is as quality a baby's book as they come.  I love this book through and through.\", \"Such a sweet book!  It has a great rhyming pattern to read, both my kids love it and gesture to read it out of the mix of books we have before they've been able to talk.  It's a good quality book, 'board'-ish pages but thinner than a traditional board book.  The story is really sweet to read to your children and it offers some great interaction pages where you can have teachable moments about body parts and actions.  Huge hit here!\", \"A sweet story of loving your little one from head to toe (literally). My son was drawn to this book since he was a baby (he's now 3 & still requests it).The pages are thick & shiny board-like, which I prefer because toddlers can't bend or rip them like regular paper pages. The front & back covers  are thick and sturdy with a slight padded feel to them.  It is very sturdy & actually looks almost new for having been heavily used over 3 years now.I've purchased it multiple times instead of a card for new babies in our family-we write a small note about sharing our favorite story!\", 'I love this book- how simple it is and shares unconditional love.  Kids need to hear that they are loved no matter what and this one starts them early. It normalizes the more difficult emotions too. I read it to my two children for years and now read to foster children who love it and need to hear the message as well. So simple but super cute.', 'Unlike the other books in the series, this book doesn’t flow as well because there’s not enough words in the pages. My son asked for it and I figured I’d buy it since I liked the others in the series and this one was on sale... wish I hadn’t, but my son likes it so I can’t return. On the plus side, he memorized it already and reads it to himself now :)']\n"
     ]
    }
   ],
   "source": [
    "all_r = soup.find_all(\"div\", class_=\"a-section celwidget\")\n",
    "all_user = []    # 사용자\n",
    "all_ratings = [] # 평점\n",
    "all_dates = []   # 날짜\n",
    "all_reviews = [] # 리뷰\n",
    "for one in all_r:\n",
    "    user_one = one.find(\"span\", class_=\"a-profile-name\").text\n",
    "    all_user.append(user_one)  # 사용자 추가\n",
    "    rating_one = one.find(\"span\", class_=\"a-icon-alt\").text\n",
    "    nums = re.findall(\"\\d+\", rating_one)[0]\n",
    "    all_ratings.append(nums)   # 평점 추가\n",
    "    date_one = one.find(\"span\", class_=\"a-size-base a-color-secondary review-date\")\n",
    "    texts = date_one.text.split(\"on\")\n",
    "    data = texts[1].strip()\n",
    "    all_dates.append(data)\n",
    "    # 리뷰 추가\n",
    "    review_one = one.find(\"span\",\n",
    "                class_=\"a-size-base review-text review-text-content\")\n",
    "    tmp = review_one.text\n",
    "    review = tmp.strip()\n",
    "    all_reviews.append(review)\n",
    "print(all_user)\n",
    "print(all_ratings)\n",
    "print(all_dates)\n",
    "print(all_reviews)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'all_rating' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-116-f50cf9f353ba>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     27\u001b[0m         \u001b[0mall_reviews\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreview\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     28\u001b[0m     \u001b[1;31m# 확인\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 29\u001b[1;33m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"user : \"\u001b[0m \u001b[1;33m,\u001b[0m \u001b[0mall_user\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"rating :\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mall_rating\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     30\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"review : \"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mall_reviews\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"\\n\\n\\n\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     31\u001b[0m     \u001b[1;31m# 다음 페이지 클릭\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'all_rating' is not defined"
     ]
    }
   ],
   "source": [
    "import time\n",
    "all_user = []    # 사용자\n",
    "all_ratings = [] # 평점\n",
    "all_dates = []   # 날짜\n",
    "all_reviews = [] # 리뷰\n",
    "for page in range(2, 7, 1):\n",
    "    time.sleep(3)\n",
    "    page = driver.page_source\n",
    "    soup = BeautifulSoup(page, 'html.parser')\n",
    "    all_r = soup.find_all(\"div\", class_=\"a-section celwidget\")\n",
    "    for one in all_r:\n",
    "        user_one = one.find(\"span\", class_=\"a-profile-name\").text\n",
    "        all_user.append(user_one)  # 사용자 추가\n",
    "        rating_one = one.find(\"span\", class_=\"a-icon-alt\").text\n",
    "        nums = re.findall(\"\\d+\", rating_one)[0]\n",
    "        all_ratings.append(nums)   # 평점 추가\n",
    "        # 날짜\n",
    "        date_one = one.find(\"span\", class_=\"a-size-base a-color-secondary review-date\")\n",
    "        texts = date_one.text.split(\"on\")\n",
    "        data = texts[1].strip()\n",
    "        all_dates.append(data)\n",
    "        # 리뷰 추가\n",
    "        review_one = one.find(\"span\",\n",
    "                    class_=\"a-size-base review-text review-text-content\")\n",
    "        tmp = review_one.text\n",
    "        review = tmp.strip()\n",
    "        all_reviews.append(review)\n",
    "    # 확인\n",
    "    print(\"user : \" , all_user[-1], \"rating :\", all_rating[-1])\n",
    "    print(\"review : \", all_review[-1], end=\"\\n\\n\\n\")\n",
    "    # 다음 페이지 클릭\n",
    "    sel_next = driver.find_element_by_xpath('//*[@id=\"cm_cr-pagination_bar\"]/ul/li[2]/a')\n",
    "    sel_next.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Amazon Customer\n",
      "Noha Anous\n",
      "2B4Elise\n",
      "Amazon Customer\n",
      "R. P.\n",
      "Top Contributor: Baby\n",
      "Sparky127\n",
      "Amazon Customer\n",
      "CK\n",
      "Anne\n",
      "Renata\n"
     ]
    }
   ],
   "source": [
    "##/div[1]/a/div[2]/span 사용자\n",
    "sel_add = driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]/div[1]/a/div[2]/span')\n",
    "for i in sel_add:\n",
    "    print(i.text)\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n",
      "\n",
      "4.0\n",
      "\n",
      "2.0\n",
      "\n",
      "5.0\n",
      "\n",
      "5.0\n",
      "\n",
      "4.0\n",
      "\n",
      "5.0\n",
      "\n",
      "5.0\n",
      "\n",
      "5.0\n",
      "\n",
      "3.0\n",
      "\n"
     ]
    }
   ],
   "source": [
    "sel_star = driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]/div[2]/a')\n",
    "for i in sel_star:\n",
    "    print(i.get_attribute('title')[:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reviewed in the United States on September 7, 2020\n",
      "Reviewed in the United States on February 8, 2021\n",
      "Reviewed in the United States on March 12, 2020\n",
      "Reviewed in the United States on September 25, 2016\n",
      "Reviewed in the United States on July 23, 2018\n",
      "Reviewed in the United States on March 16, 2012\n",
      "Reviewed in the United States on December 18, 2019\n",
      "Reviewed in the United States on August 10, 2016\n",
      "Reviewed in the United States on December 31, 2020\n",
      "Reviewed in the United States on January 14, 2021\n"
     ]
    }
   ],
   "source": [
    "sel_star = driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]/span')\n",
    "for i in sel_star:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 people found this helpful\n",
      "3 people found this helpful\n",
      "6 people found this helpful\n",
      "Helpful\n",
      "7 people found this helpful\n",
      "Helpful\n",
      "Helpful\n"
     ]
    }
   ],
   "source": [
    "sel_wow = driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]/div[5]/div/span[1]/div[1]/span')\n",
    "for i in sel_wow:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Amazon Customer\n",
      "Beautiful Book with Very Important Message but meant for Babies\n",
      "Reviewed in the United States on September 7, 2020\n",
      "Verified Purchase\n",
      "My friend told me this is a great bonding book that builds healthy attachement. She reccomended it for my 4 year old. I am not sure if there are 2 version but this is definetly not for his age. It is a beautiful cute lovely book. Love the messages & cute pictures. The pages are really nice and sturdy. comfortable cover. BUT its dissapointing cuz it's a one liner per page and he doesnt want me to read this one. I believe this is the perfect book to start reading when baby is a few months and then maybe if you read it so many times then by 4 a child will still love it because it is familiar, there are many bonding moments/memories associated with the book. I wish they had a version for older kids. I didnt return it cuz its a good quality book and it was a very good price. and I am still hoping my son will start enjoying it because the message is so great and so important. I doubt it though. This is really a 5 star book but for me its a 2-3 stars cuz just doesnt work for me.\n",
      "2 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "Noha Anous\n",
      "Some creepy lines, but overall a lovely book\n",
      "Reviewed in the United States on February 8, 2021\n",
      "Verified Purchase\n",
      "My son loves the book. I understand it’s about opposites, but I find the phrases ‘I love your top side ‘ and ‘I love your bottom side’ really strange. If my son repeats these phrases infront of any stranger, they would say why is this kid creepy!\n",
      "Otherwise, the book is nice with nice pictures and good material that my son can open the book and turn pages on his own. My son is 2.5 years.\n",
      "\n",
      "\n",
      "4 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "2B4Elise\n",
      "Very simplistic\n",
      "Reviewed in the United States on March 12, 2020\n",
      "Verified Purchase\n",
      "I get that any book for a baby should be simple, but this one is a bit too much so. There are other books (I Love You Because You're You) that communicate unconditional love, but in a rhythmic way that's fun to read to a baby. On the plus side, the pictures are clear and simple, and I think some infants might like that. Still, I'm a bit puzzled by all the 5 star ratings.\n",
      "3 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "Amazon Customer\n",
      "Adorable book\n",
      "Reviewed in the United States on September 25, 2016\n",
      "Verified Purchase\n",
      "What an adorable book!\n",
      "So many children's books have terrible story lines or messages in them, but definitely not the case with this book. It's a very simple book with no story, just about how you love (and always will love) every part and aspect of your baby. It can teach kids some body parts (like fingers, toes, ears, nose, hair, eyes), too. It rhymes, too.\n",
      "\n",
      "The only negative is, for a board book, the pages aren't very sturdy. The pages are maybe a third or half the thickness of other board books we own. Hopefully it'll hold up, because I am sure we will be reading this book frequently!\n",
      "6 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "R. P.Top Contributor: Baby\n",
      "Reading everyday for 6 Months Straight!\n",
      "Reviewed in the United States on July 23, 2018\n",
      "Verified Purchase\n",
      "Absolutely beautify book to read to your child. The premise is so touching and our baby just loves this book. We have been reading it everyday since the day he was born.\n",
      "\n",
      "7 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "Sparky127\n",
      "Sweet, simple, wonderful book\n",
      "Reviewed in the United States on March 16, 2012\n",
      "Verified Purchase\n",
      "We absolutely love this book.\n",
      "\n",
      "It's been our son's favorite since he was about 9 months old. The pictures are beautiful, colorful, and simple. Not boring, not crowded, just what it should be. The text is sweet and simple, the rhymes are thoughtful and not dumb (you know those books!), and the sentences are short enough to hold a baby's attention so we have time to get all the words out before he turns the page.\n",
      "\n",
      "The one downside is that this book is really cheaply made. The cover is nice and padded, but the pages are cheap. The pages are thinner than other board book pages, but the bigger problem is the actual surface of the pages. Our son - an impressive drooler and finger-sucker - loves to turn the pages himself with his drool-y fingers and sometimes kiss the pages too. What I didn't learn until too late is that you can't do that with this book. For our other board books, you can get some drool on them and it just makes the pages stick together a little bit but that's it. For this book, drool made the pages stick together so much that when you separated them later, the paper tore. (See my pics in the photo gallery for examples) I'm thinking that we can't be the only parents with a drooly baby, right??\n",
      "\n",
      "Quality notwithstanding, this is as quality a baby's book as they come. I love this book through and through.\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "54 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "Amazon Customer\n",
      "a favorite read in our house\n",
      "Reviewed in the United States on December 18, 2019\n",
      "Verified Purchase\n",
      "Such a sweet book! It has a great rhyming pattern to read, both my kids love it and gesture to read it out of the mix of books we have before they've been able to talk. It's a good quality book, 'board'-ish pages but thinner than a traditional board book. The story is really sweet to read to your children and it offers some great interaction pages where you can have teachable moments about body parts and actions. Huge hit here!\n",
      "Helpful\n",
      "Report abuse\n",
      "CK\n",
      "A favorite in our house\n",
      "Reviewed in the United States on August 10, 2016\n",
      "Verified Purchase\n",
      "A sweet story of loving your little one from head to toe (literally). My son was drawn to this book since he was a baby (he's now 3 & still requests it).\n",
      "\n",
      "The pages are thick & shiny board-like, which I prefer because toddlers can't bend or rip them like regular paper pages. The front & back covers are thick and sturdy with a slight padded feel to them. It is very sturdy & actually looks almost new for having been heavily used over 3 years now.\n",
      "\n",
      "I've purchased it multiple times instead of a card for new babies in our family-we write a small note about sharing our favorite story!\n",
      "7 people found this helpful\n",
      "Helpful\n",
      "Report abuse\n",
      "Anne\n",
      "Kids need to know this!\n",
      "Reviewed in the United States on December 31, 2020\n",
      "Verified Purchase\n",
      "I love this book- how simple it is and shares unconditional love. Kids need to hear that they are loved no matter what and this one starts them early. It normalizes the more difficult emotions too. I read it to my two children for years and now read to foster children who love it and need to hear the message as well. So simple but super cute.\n",
      "Helpful\n",
      "Report abuse\n",
      "Renata\n",
      "Too simple\n",
      "Reviewed in the United States on January 14, 2021\n",
      "Verified Purchase\n",
      "Unlike the other books in the series, this book doesn’t flow as well because there’s not enough words in the pages. My son asked for it and I figured I’d buy it since I liked the others in the series and this one was on sale... wish I hadn’t, but my son likes it so I can’t return. On the plus side, he memorized it already and reads it to himself now :)\n",
      "Helpful\n",
      "Report abuse\n"
     ]
    }
   ],
   "source": [
    "##/div[1]/a/div[2]/span 사용자\n",
    "sel_add = driver.find_elements_by_xpath('//*[@class=\"a-section celwidget\"]')\n",
    "for i in sel_add:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome('chromedriver')\n",
    "url = 'https://www.amazon.com/Samsung-Chromebook-Plus-Camera-Chrome/product-reviews/B07J1SY5QQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "273 people found this helpful\n",
      "207 people found this helpful\n",
      "180 people found this helpful\n",
      "126 people found this helpful\n",
      "148 people found this helpful\n",
      "138 people found this helpful\n",
      "135 people found this helpful\n",
      "82 people found this helpful\n",
      "85 people found this helpful\n",
      "71 people found this helpful\n"
     ]
    }
   ],
   "source": [
    "all_user = []\n",
    "all_star = []\n",
    "all_date = []\n",
    "all_review = []\n",
    "page = driver.page_source\n",
    "soup = BeautifulSoup(page,'html.parser')\n",
    "reviews = soup.select('#cm_cr-review_list > div')\n",
    "for review in reviews:\n",
    "    try:\n",
    "        iname=review.select_one('div.a-profile-content > span').text\n",
    "        istar=review.select_one('div:nth-child(2) > a:nth-child(1) > i > span').text\n",
    "        idate=review.select_one('span.a-size-base').text\n",
    "        iview=review.select_one('span.a-size-base > span').text\n",
    "        icount=review.select_one('span.cr-vote > div.a-row.a-spacing-small > span').text\n",
    "        all_user.append(iname)\n",
    "        all_star.append(istar)\n",
    "        all_date.append(idate)\n",
    "        all_review.append(iview)\n",
    "        print(icount)\n",
    "    except Exception as e:\n",
    "        continue\n",
    "  \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "dict_doc = {'user' : all_user, 'star' : all_star, 'date' : all_date, 'review' : all_review}\n",
    "doc = pd.DataFrame(dict_doc)\n",
    "doc.to_csv(\"리뷰모음.csv\", index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "273\n",
      "207\n",
      "180\n",
      "126\n",
      "148\n",
      "138\n",
      "135\n",
      "82 \n",
      "85 \n",
      "71 \n"
     ]
    }
   ],
   "source": [
    "reviews = soup.select('#cm_cr-review_list > div')\n",
    "for review in reviews:\n",
    "    try:\n",
    "        iname=review.select_one('div.a-profile-content > span').text\n",
    "        istar=review.select_one('div:nth-child(2) > a:nth-child(1) > i > span').text\n",
    "        idate=review.select_one('span.a-size-base').text\n",
    "        iview=review.select_one('span.a-size-base > span').text\n",
    "        icount=review.select_one('span.cr-vote > div.a-row.a-spacing-small > span').text\n",
    "        print(icount[:3])\n",
    "    except Exception as e:\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
