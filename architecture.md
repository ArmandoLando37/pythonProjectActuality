Structure du dossier pour le volume data
Le numÚro de sÚrie du volume est B8A9-4B78
D:.
|   .env
|   .gitignore
|   analysis.py
|   api.py
|   architecture.md
|   articles_20261029_131419.pdf
|   env.exemple
|   main.py
|   pdf_exporter.py
|   README.md
|   requirements.txt
|   
+---core
|       export_manager.py
|       favorites_manager.py
|       theme_manager.py
|       __init__.py
|       
+---disign
|       006220fdd4c9773c516b70cf2758c743.webp
|       
+---resources
|       logo.png
|       style.css
|       
+---ui
|   |   article_detail.py
|   |   components.py
|   |   
|   \---__pycache__
|           article_detail.cpython-312.pyc
|           components.cpython-312.pyc
|           
+---venv
|   |   .gitignore
|   |   .lock
|   |   CACHEDIR.TAG
|   |   pyvenv.cfg
|   |   
|   +---Lib
|   |   \---site-packages
|   |       |   pylab.py
|   |       |   six.py
|   |       |   
|   |       +---certifi
|   |       |   |   cacert.pem
|   |       |   |   core.py
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           core.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---certifi-2025.8.3.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---charset_normalizer
|   |       |   |   api.py
|   |       |   |   cd.py
|   |       |   |   constant.py
|   |       |   |   legacy.py
|   |       |   |   md.cp312-win_amd64.pyd
|   |       |   |   md.py
|   |       |   |   md__mypyc.cp312-win_amd64.pyd
|   |       |   |   models.py
|   |       |   |   py.typed
|   |       |   |   utils.py
|   |       |   |   version.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---cli
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   \---__pycache__
|   |       |           api.cpython-312.pyc
|   |       |           cd.cpython-312.pyc
|   |       |           constant.cpython-312.pyc
|   |       |           legacy.cpython-312.pyc
|   |       |           models.cpython-312.pyc
|   |       |           utils.cpython-312.pyc
|   |       |           version.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---charset_normalizer-3.4.3.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---contourpy
|   |       |   |   array.py
|   |       |   |   chunk.py
|   |       |   |   convert.py
|   |       |   |   dechunk.py
|   |       |   |   enum_util.py
|   |       |   |   py.typed
|   |       |   |   typecheck.py
|   |       |   |   types.py
|   |       |   |   _contourpy.cp312-win_amd64.lib
|   |       |   |   _contourpy.cp312-win_amd64.pyd
|   |       |   |   _contourpy.pyi
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---util
|   |       |           bokeh_renderer.py
|   |       |           bokeh_util.py
|   |       |           data.py
|   |       |           mpl_renderer.py
|   |       |           mpl_util.py
|   |       |           renderer.py
|   |       |           _build_config.py
|   |       |           __init__.py
|   |       |           
|   |       +---contourpy-1.3.3.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---cycler
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---cycler-0.12.1.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       
|   |       +---dateutil
|   |       |   |   easter.py
|   |       |   |   relativedelta.py
|   |       |   |   rrule.py
|   |       |   |   tzwin.py
|   |       |   |   utils.py
|   |       |   |   _common.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---parser
|   |       |   |   |   isoparser.py
|   |       |   |   |   _parser.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           isoparser.cpython-312.pyc
|   |       |   |           _parser.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---tz
|   |       |   |   |   tz.py
|   |       |   |   |   win.py
|   |       |   |   |   _common.py
|   |       |   |   |   _factories.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           tz.cpython-312.pyc
|   |       |   |           win.cpython-312.pyc
|   |       |   |           _common.cpython-312.pyc
|   |       |   |           _factories.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---zoneinfo
|   |       |   |       dateutil-zoneinfo.tar.gz
|   |       |   |       rebuild.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   \---__pycache__
|   |       |           relativedelta.cpython-312.pyc
|   |       |           rrule.cpython-312.pyc
|   |       |           _common.cpython-312.pyc
|   |       |           _version.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---dotenv
|   |       |   |   cli.py
|   |       |   |   ipython.py
|   |       |   |   main.py
|   |       |   |   parser.py
|   |       |   |   py.typed
|   |       |   |   variables.py
|   |       |   |   version.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           main.cpython-312.pyc
|   |       |           parser.cpython-312.pyc
|   |       |           variables.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---fontTools
|   |       |   |   afmLib.py
|   |       |   |   agl.py
|   |       |   |   fontBuilder.py
|   |       |   |   help.py
|   |       |   |   tfmLib.py
|   |       |   |   ttx.py
|   |       |   |   unicode.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---cffLib
|   |       |   |       CFF2ToCFF.py
|   |       |   |       CFFToCFF2.py
|   |       |   |       specializer.py
|   |       |   |       transforms.py
|   |       |   |       width.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---colorLib
|   |       |   |       builder.py
|   |       |   |       errors.py
|   |       |   |       geometry.py
|   |       |   |       table_builder.py
|   |       |   |       unbuilder.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---config
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---cu2qu
|   |       |   |       benchmark.py
|   |       |   |       cli.py
|   |       |   |       cu2qu.c
|   |       |   |       cu2qu.cp312-win_amd64.pyd
|   |       |   |       cu2qu.py
|   |       |   |       errors.py
|   |       |   |       ufo.py
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---designspaceLib
|   |       |   |       split.py
|   |       |   |       statNames.py
|   |       |   |       types.py
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---encodings
|   |       |   |       codecs.py
|   |       |   |       MacRoman.py
|   |       |   |       StandardEncoding.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---feaLib
|   |       |   |       ast.py
|   |       |   |       builder.py
|   |       |   |       error.py
|   |       |   |       lexer.c
|   |       |   |       lexer.cp312-win_amd64.pyd
|   |       |   |       lexer.py
|   |       |   |       location.py
|   |       |   |       lookupDebugInfo.py
|   |       |   |       parser.py
|   |       |   |       variableScalar.py
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---merge
|   |       |   |       base.py
|   |       |   |       cmap.py
|   |       |   |       layout.py
|   |       |   |       options.py
|   |       |   |       tables.py
|   |       |   |       unicode.py
|   |       |   |       util.py
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---misc
|   |       |   |   |   arrayTools.py
|   |       |   |   |   bezierTools.c
|   |       |   |   |   bezierTools.cp312-win_amd64.pyd
|   |       |   |   |   bezierTools.py
|   |       |   |   |   classifyTools.py
|   |       |   |   |   cliTools.py
|   |       |   |   |   configTools.py
|   |       |   |   |   cython.py
|   |       |   |   |   dictTools.py
|   |       |   |   |   eexec.py
|   |       |   |   |   encodingTools.py
|   |       |   |   |   etree.py
|   |       |   |   |   filenames.py
|   |       |   |   |   fixedTools.py
|   |       |   |   |   intTools.py
|   |       |   |   |   iterTools.py
|   |       |   |   |   lazyTools.py
|   |       |   |   |   loggingTools.py
|   |       |   |   |   macCreatorType.py
|   |       |   |   |   macRes.py
|   |       |   |   |   psCharStrings.py
|   |       |   |   |   psLib.py
|   |       |   |   |   psOperators.py
|   |       |   |   |   py23.py
|   |       |   |   |   roundTools.py
|   |       |   |   |   sstruct.py
|   |       |   |   |   symfont.py
|   |       |   |   |   testTools.py
|   |       |   |   |   textTools.py
|   |       |   |   |   timeTools.py
|   |       |   |   |   transform.py
|   |       |   |   |   treeTools.py
|   |       |   |   |   vector.py
|   |       |   |   |   visitor.py
|   |       |   |   |   xmlReader.py
|   |       |   |   |   xmlWriter.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---filesystem
|   |       |   |   |       _base.py
|   |       |   |   |       _copy.py
|   |       |   |   |       _errors.py
|   |       |   |   |       _info.py
|   |       |   |   |       _osfs.py
|   |       |   |   |       _path.py
|   |       |   |   |       _subfs.py
|   |       |   |   |       _tempfs.py
|   |       |   |   |       _tools.py
|   |       |   |   |       _walk.py
|   |       |   |   |       _zipfs.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---plistlib
|   |       |   |           py.typed
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---mtiLib
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---otlLib
|   |       |   |   |   builder.py
|   |       |   |   |   error.py
|   |       |   |   |   maxContextCalc.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---optimize
|   |       |   |           gpos.py
|   |       |   |           __init__.py
|   |       |   |           __main__.py
|   |       |   |           
|   |       |   +---pens
|   |       |   |       areaPen.py
|   |       |   |       basePen.py
|   |       |   |       boundsPen.py
|   |       |   |       cairoPen.py
|   |       |   |       cocoaPen.py
|   |       |   |       cu2quPen.py
|   |       |   |       explicitClosingLinePen.py
|   |       |   |       filterPen.py
|   |       |   |       freetypePen.py
|   |       |   |       hashPointPen.py
|   |       |   |       momentsPen.c
|   |       |   |       momentsPen.cp312-win_amd64.pyd
|   |       |   |       momentsPen.py
|   |       |   |       perimeterPen.py
|   |       |   |       pointInsidePen.py
|   |       |   |       pointPen.py
|   |       |   |       qtPen.py
|   |       |   |       qu2cuPen.py
|   |       |   |       quartzPen.py
|   |       |   |       recordingPen.py
|   |       |   |       reportLabPen.py
|   |       |   |       reverseContourPen.py
|   |       |   |       roundingPen.py
|   |       |   |       statisticsPen.py
|   |       |   |       svgPathPen.py
|   |       |   |       t2CharStringPen.py
|   |       |   |       teePen.py
|   |       |   |       transformPen.py
|   |       |   |       ttGlyphPen.py
|   |       |   |       wxPen.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---qu2cu
|   |       |   |       benchmark.py
|   |       |   |       cli.py
|   |       |   |       qu2cu.c
|   |       |   |       qu2cu.cp312-win_amd64.pyd
|   |       |   |       qu2cu.py
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---subset
|   |       |   |       cff.py
|   |       |   |       svg.py
|   |       |   |       util.py
|   |       |   |       __init__.py
|   |       |   |       __main__.py
|   |       |   |       
|   |       |   +---svgLib
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---path
|   |       |   |           arc.py
|   |       |   |           parser.py
|   |       |   |           shapes.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---t1Lib
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---ttLib
|   |       |   |   |   macUtils.py
|   |       |   |   |   removeOverlaps.py
|   |       |   |   |   reorderGlyphs.py
|   |       |   |   |   scaleUpem.py
|   |       |   |   |   sfnt.py
|   |       |   |   |   standardGlyphOrder.py
|   |       |   |   |   ttCollection.py
|   |       |   |   |   ttFont.py
|   |       |   |   |   ttGlyphSet.py
|   |       |   |   |   ttVisitor.py
|   |       |   |   |   woff2.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __main__.py
|   |       |   |   |   
|   |       |   |   \---tables
|   |       |   |           asciiTable.py
|   |       |   |           BitmapGlyphMetrics.py
|   |       |   |           B_A_S_E_.py
|   |       |   |           C_B_D_T_.py
|   |       |   |           C_B_L_C_.py
|   |       |   |           C_F_F_.py
|   |       |   |           C_F_F__2.py
|   |       |   |           C_O_L_R_.py
|   |       |   |           C_P_A_L_.py
|   |       |   |           DefaultTable.py
|   |       |   |           D_S_I_G_.py
|   |       |   |           D__e_b_g.py
|   |       |   |           E_B_D_T_.py
|   |       |   |           E_B_L_C_.py
|   |       |   |           F_F_T_M_.py
|   |       |   |           F__e_a_t.py
|   |       |   |           grUtils.py
|   |       |   |           G_D_E_F_.py
|   |       |   |           G_M_A_P_.py
|   |       |   |           G_P_K_G_.py
|   |       |   |           G_P_O_S_.py
|   |       |   |           G_S_U_B_.py
|   |       |   |           G_V_A_R_.py
|   |       |   |           G__l_a_t.py
|   |       |   |           G__l_o_c.py
|   |       |   |           H_V_A_R_.py
|   |       |   |           J_S_T_F_.py
|   |       |   |           L_T_S_H_.py
|   |       |   |           M_A_T_H_.py
|   |       |   |           M_E_T_A_.py
|   |       |   |           M_V_A_R_.py
|   |       |   |           otBase.py
|   |       |   |           otConverters.py
|   |       |   |           otData.py
|   |       |   |           otTables.py
|   |       |   |           otTraverse.py
|   |       |   |           O_S_2f_2.py
|   |       |   |           sbixGlyph.py
|   |       |   |           sbixStrike.py
|   |       |   |           S_I_N_G_.py
|   |       |   |           S_T_A_T_.py
|   |       |   |           S_V_G_.py
|   |       |   |           S__i_l_f.py
|   |       |   |           S__i_l_l.py
|   |       |   |           table_API_readme.txt
|   |       |   |           ttProgram.py
|   |       |   |           TupleVariation.py
|   |       |   |           T_S_I_B_.py
|   |       |   |           T_S_I_C_.py
|   |       |   |           T_S_I_D_.py
|   |       |   |           T_S_I_J_.py
|   |       |   |           T_S_I_P_.py
|   |       |   |           T_S_I_S_.py
|   |       |   |           T_S_I_V_.py
|   |       |   |           T_S_I__0.py
|   |       |   |           T_S_I__1.py
|   |       |   |           T_S_I__2.py
|   |       |   |           T_S_I__3.py
|   |       |   |           T_S_I__5.py
|   |       |   |           T_T_F_A_.py
|   |       |   |           V_A_R_C_.py
|   |       |   |           V_D_M_X_.py
|   |       |   |           V_O_R_G_.py
|   |       |   |           V_V_A_R_.py
|   |       |   |           _a_n_k_r.py
|   |       |   |           _a_v_a_r.py
|   |       |   |           _b_s_l_n.py
|   |       |   |           _c_i_d_g.py
|   |       |   |           _c_m_a_p.py
|   |       |   |           _c_v_a_r.py
|   |       |   |           _c_v_t.py
|   |       |   |           _f_e_a_t.py
|   |       |   |           _f_p_g_m.py
|   |       |   |           _f_v_a_r.py
|   |       |   |           _g_a_s_p.py
|   |       |   |           _g_c_i_d.py
|   |       |   |           _g_l_y_f.py
|   |       |   |           _g_v_a_r.py
|   |       |   |           _h_d_m_x.py
|   |       |   |           _h_e_a_d.py
|   |       |   |           _h_h_e_a.py
|   |       |   |           _h_m_t_x.py
|   |       |   |           _k_e_r_n.py
|   |       |   |           _l_c_a_r.py
|   |       |   |           _l_o_c_a.py
|   |       |   |           _l_t_a_g.py
|   |       |   |           _m_a_x_p.py
|   |       |   |           _m_e_t_a.py
|   |       |   |           _m_o_r_t.py
|   |       |   |           _m_o_r_x.py
|   |       |   |           _n_a_m_e.py
|   |       |   |           _o_p_b_d.py
|   |       |   |           _p_o_s_t.py
|   |       |   |           _p_r_e_p.py
|   |       |   |           _p_r_o_p.py
|   |       |   |           _s_b_i_x.py
|   |       |   |           _t_r_a_k.py
|   |       |   |           _v_h_e_a.py
|   |       |   |           _v_m_t_x.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---ufoLib
|   |       |   |       converters.py
|   |       |   |       errors.py
|   |       |   |       etree.py
|   |       |   |       filenames.py
|   |       |   |       glifLib.py
|   |       |   |       kerning.py
|   |       |   |       plistlib.py
|   |       |   |       pointPen.py
|   |       |   |       utils.py
|   |       |   |       validators.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---unicodedata
|   |       |   |       Blocks.py
|   |       |   |       Mirrored.py
|   |       |   |       OTTags.py
|   |       |   |       ScriptExtensions.py
|   |       |   |       Scripts.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---varLib
|   |       |   |   |   avar.py
|   |       |   |   |   avarPlanner.py
|   |       |   |   |   builder.py
|   |       |   |   |   cff.py
|   |       |   |   |   errors.py
|   |       |   |   |   featureVars.py
|   |       |   |   |   hvar.py
|   |       |   |   |   interpolatable.py
|   |       |   |   |   interpolatableHelpers.py
|   |       |   |   |   interpolatablePlot.py
|   |       |   |   |   interpolatableTestContourOrder.py
|   |       |   |   |   interpolatableTestStartingPoint.py
|   |       |   |   |   interpolate_layout.py
|   |       |   |   |   iup.c
|   |       |   |   |   iup.cp312-win_amd64.pyd
|   |       |   |   |   iup.py
|   |       |   |   |   merger.py
|   |       |   |   |   models.py
|   |       |   |   |   multiVarStore.py
|   |       |   |   |   mutator.py
|   |       |   |   |   mvar.py
|   |       |   |   |   plot.py
|   |       |   |   |   stat.py
|   |       |   |   |   varStore.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __main__.py
|   |       |   |   |   
|   |       |   |   \---instancer
|   |       |   |           featureVars.py
|   |       |   |           names.py
|   |       |   |           solver.py
|   |       |   |           __init__.py
|   |       |   |           __main__.py
|   |       |   |           
|   |       |   \---voltLib
|   |       |           ast.py
|   |       |           error.py
|   |       |           lexer.py
|   |       |           parser.py
|   |       |           voltToFea.py
|   |       |           __init__.py
|   |       |           __main__.py
|   |       |           
|   |       +---fonttools-4.59.2.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           LICENSE.external
|   |       |           
|   |       +---idna
|   |       |   |   codec.py
|   |       |   |   compat.py
|   |       |   |   core.py
|   |       |   |   idnadata.py
|   |       |   |   intranges.py
|   |       |   |   package_data.py
|   |       |   |   py.typed
|   |       |   |   uts46data.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           core.cpython-312.pyc
|   |       |           idnadata.cpython-312.pyc
|   |       |           intranges.cpython-312.pyc
|   |       |           package_data.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---idna-3.10.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE.md
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---kiwisolver
|   |       |   |   exceptions.py
|   |       |   |   py.typed
|   |       |   |   _cext.cp312-win_amd64.pyd
|   |       |   |   _cext.pyi
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           exceptions.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---kiwisolver-1.4.9.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---matplotlib
|   |       |   |   animation.py
|   |       |   |   animation.pyi
|   |       |   |   artist.py
|   |       |   |   artist.pyi
|   |       |   |   axis.py
|   |       |   |   axis.pyi
|   |       |   |   backend_bases.py
|   |       |   |   backend_bases.pyi
|   |       |   |   backend_managers.py
|   |       |   |   backend_managers.pyi
|   |       |   |   backend_tools.py
|   |       |   |   backend_tools.pyi
|   |       |   |   bezier.py
|   |       |   |   bezier.pyi
|   |       |   |   category.py
|   |       |   |   cbook.py
|   |       |   |   cbook.pyi
|   |       |   |   cm.py
|   |       |   |   cm.pyi
|   |       |   |   collections.py
|   |       |   |   collections.pyi
|   |       |   |   colorbar.py
|   |       |   |   colorbar.pyi
|   |       |   |   colorizer.py
|   |       |   |   colorizer.pyi
|   |       |   |   colors.py
|   |       |   |   colors.pyi
|   |       |   |   container.py
|   |       |   |   container.pyi
|   |       |   |   contour.py
|   |       |   |   contour.pyi
|   |       |   |   dates.py
|   |       |   |   dviread.py
|   |       |   |   dviread.pyi
|   |       |   |   figure.py
|   |       |   |   figure.pyi
|   |       |   |   font_manager.py
|   |       |   |   font_manager.pyi
|   |       |   |   ft2font.cp312-win_amd64.pyd
|   |       |   |   ft2font.pyi
|   |       |   |   gridspec.py
|   |       |   |   gridspec.pyi
|   |       |   |   hatch.py
|   |       |   |   hatch.pyi
|   |       |   |   image.py
|   |       |   |   image.pyi
|   |       |   |   inset.py
|   |       |   |   inset.pyi
|   |       |   |   layout_engine.py
|   |       |   |   layout_engine.pyi
|   |       |   |   legend.py
|   |       |   |   legend.pyi
|   |       |   |   legend_handler.py
|   |       |   |   legend_handler.pyi
|   |       |   |   lines.py
|   |       |   |   lines.pyi
|   |       |   |   markers.py
|   |       |   |   markers.pyi
|   |       |   |   mathtext.py
|   |       |   |   mathtext.pyi
|   |       |   |   mlab.py
|   |       |   |   mlab.pyi
|   |       |   |   offsetbox.py
|   |       |   |   offsetbox.pyi
|   |       |   |   patches.py
|   |       |   |   patches.pyi
|   |       |   |   path.py
|   |       |   |   path.pyi
|   |       |   |   patheffects.py
|   |       |   |   patheffects.pyi
|   |       |   |   py.typed
|   |       |   |   pylab.py
|   |       |   |   pyplot.py
|   |       |   |   quiver.py
|   |       |   |   quiver.pyi
|   |       |   |   rcsetup.py
|   |       |   |   rcsetup.pyi
|   |       |   |   sankey.py
|   |       |   |   sankey.pyi
|   |       |   |   scale.py
|   |       |   |   scale.pyi
|   |       |   |   spines.py
|   |       |   |   spines.pyi
|   |       |   |   stackplot.py
|   |       |   |   stackplot.pyi
|   |       |   |   streamplot.py
|   |       |   |   streamplot.pyi
|   |       |   |   table.py
|   |       |   |   table.pyi
|   |       |   |   texmanager.py
|   |       |   |   texmanager.pyi
|   |       |   |   text.py
|   |       |   |   text.pyi
|   |       |   |   textpath.py
|   |       |   |   textpath.pyi
|   |       |   |   ticker.py
|   |       |   |   ticker.pyi
|   |       |   |   transforms.py
|   |       |   |   transforms.pyi
|   |       |   |   typing.py
|   |       |   |   units.py
|   |       |   |   widgets.py
|   |       |   |   widgets.pyi
|   |       |   |   _afm.py
|   |       |   |   _animation_data.py
|   |       |   |   _blocking_input.py
|   |       |   |   _cm.py
|   |       |   |   _cm_bivar.py
|   |       |   |   _cm_listed.py
|   |       |   |   _cm_multivar.py
|   |       |   |   _color_data.py
|   |       |   |   _color_data.pyi
|   |       |   |   _constrained_layout.py
|   |       |   |   _c_internal_utils.cp312-win_amd64.pyd
|   |       |   |   _c_internal_utils.pyi
|   |       |   |   _docstring.py
|   |       |   |   _docstring.pyi
|   |       |   |   _enums.py
|   |       |   |   _enums.pyi
|   |       |   |   _fontconfig_pattern.py
|   |       |   |   _image.cp312-win_amd64.pyd
|   |       |   |   _image.pyi
|   |       |   |   _internal_utils.py
|   |       |   |   _layoutgrid.py
|   |       |   |   _mathtext.py
|   |       |   |   _mathtext_data.py
|   |       |   |   _path.cp312-win_amd64.pyd
|   |       |   |   _path.pyi
|   |       |   |   _pylab_helpers.py
|   |       |   |   _pylab_helpers.pyi
|   |       |   |   _qhull.cp312-win_amd64.pyd
|   |       |   |   _qhull.pyi
|   |       |   |   _text_helpers.py
|   |       |   |   _tight_bbox.py
|   |       |   |   _tight_layout.py
|   |       |   |   _tri.cp312-win_amd64.pyd
|   |       |   |   _tri.pyi
|   |       |   |   _type1font.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   __init__.pyi
|   |       |   |   
|   |       |   +---axes
|   |       |   |   |   _axes.py
|   |       |   |   |   _axes.pyi
|   |       |   |   |   _base.py
|   |       |   |   |   _base.pyi
|   |       |   |   |   _secondary_axes.py
|   |       |   |   |   _secondary_axes.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _axes.cpython-312.pyc
|   |       |   |           _base.cpython-312.pyc
|   |       |   |           _secondary_axes.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---backends
|   |       |   |   |   backend_agg.py
|   |       |   |   |   backend_cairo.py
|   |       |   |   |   backend_gtk3.py
|   |       |   |   |   backend_gtk3agg.py
|   |       |   |   |   backend_gtk3cairo.py
|   |       |   |   |   backend_gtk4.py
|   |       |   |   |   backend_gtk4agg.py
|   |       |   |   |   backend_gtk4cairo.py
|   |       |   |   |   backend_macosx.py
|   |       |   |   |   backend_mixed.py
|   |       |   |   |   backend_nbagg.py
|   |       |   |   |   backend_pdf.py
|   |       |   |   |   backend_pgf.py
|   |       |   |   |   backend_ps.py
|   |       |   |   |   backend_qt.py
|   |       |   |   |   backend_qt5.py
|   |       |   |   |   backend_qt5agg.py
|   |       |   |   |   backend_qt5cairo.py
|   |       |   |   |   backend_qtagg.py
|   |       |   |   |   backend_qtcairo.py
|   |       |   |   |   backend_svg.py
|   |       |   |   |   backend_template.py
|   |       |   |   |   backend_tkagg.py
|   |       |   |   |   backend_tkcairo.py
|   |       |   |   |   backend_webagg.py
|   |       |   |   |   backend_webagg_core.py
|   |       |   |   |   backend_wx.py
|   |       |   |   |   backend_wxagg.py
|   |       |   |   |   backend_wxcairo.py
|   |       |   |   |   qt_compat.py
|   |       |   |   |   registry.py
|   |       |   |   |   _backend_agg.cp312-win_amd64.pyd
|   |       |   |   |   _backend_agg.pyi
|   |       |   |   |   _backend_gtk.py
|   |       |   |   |   _backend_pdf_ps.py
|   |       |   |   |   _backend_tk.py
|   |       |   |   |   _macosx.pyi
|   |       |   |   |   _tkagg.cp312-win_amd64.pyd
|   |       |   |   |   _tkagg.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---qt_editor
|   |       |   |   |   |   figureoptions.py
|   |       |   |   |   |   _formlayout.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           figureoptions.cpython-312.pyc
|   |       |   |   |           _formlayout.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---web_backend
|   |       |   |   |   |   all_figures.html
|   |       |   |   |   |   ipython_inline_figure.html
|   |       |   |   |   |   single_figure.html
|   |       |   |   |   |   
|   |       |   |   |   +---css
|   |       |   |   |   |       boilerplate.css
|   |       |   |   |   |       fbm.css
|   |       |   |   |   |       mpl.css
|   |       |   |   |   |       page.css
|   |       |   |   |   |       
|   |       |   |   |   \---js
|   |       |   |   |           mpl.js
|   |       |   |   |           mpl_tornado.js
|   |       |   |   |           nbagg_mpl.js
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           backend_agg.cpython-312.pyc
|   |       |   |           backend_qt.cpython-312.pyc
|   |       |   |           backend_qt5agg.cpython-312.pyc
|   |       |   |           backend_qtagg.cpython-312.pyc
|   |       |   |           qt_compat.cpython-312.pyc
|   |       |   |           registry.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---mpl-data
|   |       |   |   |   kpsewhich.lua
|   |       |   |   |   matplotlibrc
|   |       |   |   |   
|   |       |   |   +---fonts
|   |       |   |   |   +---afm
|   |       |   |   |   |       cmex10.afm
|   |       |   |   |   |       cmmi10.afm
|   |       |   |   |   |       cmr10.afm
|   |       |   |   |   |       cmsy10.afm
|   |       |   |   |   |       cmtt10.afm
|   |       |   |   |   |       pagd8a.afm
|   |       |   |   |   |       pagdo8a.afm
|   |       |   |   |   |       pagk8a.afm
|   |       |   |   |   |       pagko8a.afm
|   |       |   |   |   |       pbkd8a.afm
|   |       |   |   |   |       pbkdi8a.afm
|   |       |   |   |   |       pbkl8a.afm
|   |       |   |   |   |       pbkli8a.afm
|   |       |   |   |   |       pcrb8a.afm
|   |       |   |   |   |       pcrbo8a.afm
|   |       |   |   |   |       pcrr8a.afm
|   |       |   |   |   |       pcrro8a.afm
|   |       |   |   |   |       phvb8a.afm
|   |       |   |   |   |       phvb8an.afm
|   |       |   |   |   |       phvbo8a.afm
|   |       |   |   |   |       phvbo8an.afm
|   |       |   |   |   |       phvl8a.afm
|   |       |   |   |   |       phvlo8a.afm
|   |       |   |   |   |       phvr8a.afm
|   |       |   |   |   |       phvr8an.afm
|   |       |   |   |   |       phvro8a.afm
|   |       |   |   |   |       phvro8an.afm
|   |       |   |   |   |       pncb8a.afm
|   |       |   |   |   |       pncbi8a.afm
|   |       |   |   |   |       pncr8a.afm
|   |       |   |   |   |       pncri8a.afm
|   |       |   |   |   |       pplb8a.afm
|   |       |   |   |   |       pplbi8a.afm
|   |       |   |   |   |       pplr8a.afm
|   |       |   |   |   |       pplri8a.afm
|   |       |   |   |   |       psyr.afm
|   |       |   |   |   |       ptmb8a.afm
|   |       |   |   |   |       ptmbi8a.afm
|   |       |   |   |   |       ptmr8a.afm
|   |       |   |   |   |       ptmri8a.afm
|   |       |   |   |   |       putb8a.afm
|   |       |   |   |   |       putbi8a.afm
|   |       |   |   |   |       putr8a.afm
|   |       |   |   |   |       putri8a.afm
|   |       |   |   |   |       pzcmi8a.afm
|   |       |   |   |   |       pzdr.afm
|   |       |   |   |   |       
|   |       |   |   |   +---pdfcorefonts
|   |       |   |   |   |       Courier-Bold.afm
|   |       |   |   |   |       Courier-BoldOblique.afm
|   |       |   |   |   |       Courier-Oblique.afm
|   |       |   |   |   |       Courier.afm
|   |       |   |   |   |       Helvetica-Bold.afm
|   |       |   |   |   |       Helvetica-BoldOblique.afm
|   |       |   |   |   |       Helvetica-Oblique.afm
|   |       |   |   |   |       Helvetica.afm
|   |       |   |   |   |       readme.txt
|   |       |   |   |   |       Symbol.afm
|   |       |   |   |   |       Times-Bold.afm
|   |       |   |   |   |       Times-BoldItalic.afm
|   |       |   |   |   |       Times-Italic.afm
|   |       |   |   |   |       Times-Roman.afm
|   |       |   |   |   |       ZapfDingbats.afm
|   |       |   |   |   |       
|   |       |   |   |   \---ttf
|   |       |   |   |           cmb10.ttf
|   |       |   |   |           cmex10.ttf
|   |       |   |   |           cmmi10.ttf
|   |       |   |   |           cmr10.ttf
|   |       |   |   |           cmss10.ttf
|   |       |   |   |           cmsy10.ttf
|   |       |   |   |           cmtt10.ttf
|   |       |   |   |           DejaVuSans-Bold.ttf
|   |       |   |   |           DejaVuSans-BoldOblique.ttf
|   |       |   |   |           DejaVuSans-Oblique.ttf
|   |       |   |   |           DejaVuSans.ttf
|   |       |   |   |           DejaVuSansDisplay.ttf
|   |       |   |   |           DejaVuSansMono-Bold.ttf
|   |       |   |   |           DejaVuSansMono-BoldOblique.ttf
|   |       |   |   |           DejaVuSansMono-Oblique.ttf
|   |       |   |   |           DejaVuSansMono.ttf
|   |       |   |   |           DejaVuSerif-Bold.ttf
|   |       |   |   |           DejaVuSerif-BoldItalic.ttf
|   |       |   |   |           DejaVuSerif-Italic.ttf
|   |       |   |   |           DejaVuSerif.ttf
|   |       |   |   |           DejaVuSerifDisplay.ttf
|   |       |   |   |           LICENSE_DEJAVU
|   |       |   |   |           LICENSE_STIX
|   |       |   |   |           STIXGeneral.ttf
|   |       |   |   |           STIXGeneralBol.ttf
|   |       |   |   |           STIXGeneralBolIta.ttf
|   |       |   |   |           STIXGeneralItalic.ttf
|   |       |   |   |           STIXNonUni.ttf
|   |       |   |   |           STIXNonUniBol.ttf
|   |       |   |   |           STIXNonUniBolIta.ttf
|   |       |   |   |           STIXNonUniIta.ttf
|   |       |   |   |           STIXSizFiveSymReg.ttf
|   |       |   |   |           STIXSizFourSymBol.ttf
|   |       |   |   |           STIXSizFourSymReg.ttf
|   |       |   |   |           STIXSizOneSymBol.ttf
|   |       |   |   |           STIXSizOneSymReg.ttf
|   |       |   |   |           STIXSizThreeSymBol.ttf
|   |       |   |   |           STIXSizThreeSymReg.ttf
|   |       |   |   |           STIXSizTwoSymBol.ttf
|   |       |   |   |           STIXSizTwoSymReg.ttf
|   |       |   |   |           
|   |       |   |   +---images
|   |       |   |   |       back-symbolic.svg
|   |       |   |   |       back.pdf
|   |       |   |   |       back.png
|   |       |   |   |       back.svg
|   |       |   |   |       back_large.png
|   |       |   |   |       filesave-symbolic.svg
|   |       |   |   |       filesave.pdf
|   |       |   |   |       filesave.png
|   |       |   |   |       filesave.svg
|   |       |   |   |       filesave_large.png
|   |       |   |   |       forward-symbolic.svg
|   |       |   |   |       forward.pdf
|   |       |   |   |       forward.png
|   |       |   |   |       forward.svg
|   |       |   |   |       forward_large.png
|   |       |   |   |       hand.pdf
|   |       |   |   |       hand.png
|   |       |   |   |       hand.svg
|   |       |   |   |       help-symbolic.svg
|   |       |   |   |       help.pdf
|   |       |   |   |       help.png
|   |       |   |   |       help.svg
|   |       |   |   |       help_large.png
|   |       |   |   |       home-symbolic.svg
|   |       |   |   |       home.pdf
|   |       |   |   |       home.png
|   |       |   |   |       home.svg
|   |       |   |   |       home_large.png
|   |       |   |   |       matplotlib.pdf
|   |       |   |   |       matplotlib.png
|   |       |   |   |       matplotlib.svg
|   |       |   |   |       matplotlib_large.png
|   |       |   |   |       move-symbolic.svg
|   |       |   |   |       move.pdf
|   |       |   |   |       move.png
|   |       |   |   |       move.svg
|   |       |   |   |       move_large.png
|   |       |   |   |       qt4_editor_options.pdf
|   |       |   |   |       qt4_editor_options.png
|   |       |   |   |       qt4_editor_options.svg
|   |       |   |   |       qt4_editor_options_large.png
|   |       |   |   |       subplots-symbolic.svg
|   |       |   |   |       subplots.pdf
|   |       |   |   |       subplots.png
|   |       |   |   |       subplots.svg
|   |       |   |   |       subplots_large.png
|   |       |   |   |       zoom_to_rect-symbolic.svg
|   |       |   |   |       zoom_to_rect.pdf
|   |       |   |   |       zoom_to_rect.png
|   |       |   |   |       zoom_to_rect.svg
|   |       |   |   |       zoom_to_rect_large.png
|   |       |   |   |       
|   |       |   |   +---plot_directive
|   |       |   |   |       plot_directive.css
|   |       |   |   |       
|   |       |   |   +---sample_data
|   |       |   |   |   |   data_x_x2_x3.csv
|   |       |   |   |   |   eeg.dat
|   |       |   |   |   |   embedding_in_wx3.xrc
|   |       |   |   |   |   goog.npz
|   |       |   |   |   |   grace_hopper.jpg
|   |       |   |   |   |   jacksboro_fault_dem.npz
|   |       |   |   |   |   logo2.png
|   |       |   |   |   |   membrane.dat
|   |       |   |   |   |   Minduka_Present_Blue_Pack.png
|   |       |   |   |   |   msft.csv
|   |       |   |   |   |   README.txt
|   |       |   |   |   |   s1045.ima.gz
|   |       |   |   |   |   Stocks.csv
|   |       |   |   |   |   topobathy.npz
|   |       |   |   |   |   
|   |       |   |   |   \---axes_grid
|   |       |   |   |           bivariate_normal.npy
|   |       |   |   |           
|   |       |   |   \---stylelib
|   |       |   |           bmh.mplstyle
|   |       |   |           classic.mplstyle
|   |       |   |           dark_background.mplstyle
|   |       |   |           fast.mplstyle
|   |       |   |           fivethirtyeight.mplstyle
|   |       |   |           ggplot.mplstyle
|   |       |   |           grayscale.mplstyle
|   |       |   |           petroff10.mplstyle
|   |       |   |           seaborn-v0_8-bright.mplstyle
|   |       |   |           seaborn-v0_8-colorblind.mplstyle
|   |       |   |           seaborn-v0_8-dark-palette.mplstyle
|   |       |   |           seaborn-v0_8-dark.mplstyle
|   |       |   |           seaborn-v0_8-darkgrid.mplstyle
|   |       |   |           seaborn-v0_8-deep.mplstyle
|   |       |   |           seaborn-v0_8-muted.mplstyle
|   |       |   |           seaborn-v0_8-notebook.mplstyle
|   |       |   |           seaborn-v0_8-paper.mplstyle
|   |       |   |           seaborn-v0_8-pastel.mplstyle
|   |       |   |           seaborn-v0_8-poster.mplstyle
|   |       |   |           seaborn-v0_8-talk.mplstyle
|   |       |   |           seaborn-v0_8-ticks.mplstyle
|   |       |   |           seaborn-v0_8-white.mplstyle
|   |       |   |           seaborn-v0_8-whitegrid.mplstyle
|   |       |   |           seaborn-v0_8.mplstyle
|   |       |   |           Solarize_Light2.mplstyle
|   |       |   |           tableau-colorblind10.mplstyle
|   |       |   |           _classic_test_patch.mplstyle
|   |       |   |           _mpl-gallery-nogrid.mplstyle
|   |       |   |           _mpl-gallery.mplstyle
|   |       |   |           
|   |       |   +---projections
|   |       |   |   |   geo.py
|   |       |   |   |   geo.pyi
|   |       |   |   |   polar.py
|   |       |   |   |   polar.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           geo.cpython-312.pyc
|   |       |   |           polar.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---sphinxext
|   |       |   |       figmpl_directive.py
|   |       |   |       mathmpl.py
|   |       |   |       plot_directive.py
|   |       |   |       roles.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---style
|   |       |   |   |   core.py
|   |       |   |   |   core.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           core.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---testing
|   |       |   |   |   compare.py
|   |       |   |   |   compare.pyi
|   |       |   |   |   conftest.py
|   |       |   |   |   conftest.pyi
|   |       |   |   |   decorators.py
|   |       |   |   |   decorators.pyi
|   |       |   |   |   exceptions.py
|   |       |   |   |   widgets.py
|   |       |   |   |   widgets.pyi
|   |       |   |   |   _markers.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---jpl_units
|   |       |   |           Duration.py
|   |       |   |           Epoch.py
|   |       |   |           EpochConverter.py
|   |       |   |           StrConverter.py
|   |       |   |           UnitDbl.py
|   |       |   |           UnitDblConverter.py
|   |       |   |           UnitDblFormatter.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---tests
|   |       |   |       conftest.py
|   |       |   |       test_afm.py
|   |       |   |       test_agg.py
|   |       |   |       test_agg_filter.py
|   |       |   |       test_animation.py
|   |       |   |       test_api.py
|   |       |   |       test_arrow_patches.py
|   |       |   |       test_artist.py
|   |       |   |       test_axes.py
|   |       |   |       test_axis.py
|   |       |   |       test_backends_interactive.py
|   |       |   |       test_backend_bases.py
|   |       |   |       test_backend_cairo.py
|   |       |   |       test_backend_gtk3.py
|   |       |   |       test_backend_inline.py
|   |       |   |       test_backend_macosx.py
|   |       |   |       test_backend_nbagg.py
|   |       |   |       test_backend_pdf.py
|   |       |   |       test_backend_pgf.py
|   |       |   |       test_backend_ps.py
|   |       |   |       test_backend_qt.py
|   |       |   |       test_backend_registry.py
|   |       |   |       test_backend_svg.py
|   |       |   |       test_backend_template.py
|   |       |   |       test_backend_tk.py
|   |       |   |       test_backend_tools.py
|   |       |   |       test_backend_webagg.py
|   |       |   |       test_basic.py
|   |       |   |       test_bbox_tight.py
|   |       |   |       test_bezier.py
|   |       |   |       test_category.py
|   |       |   |       test_cbook.py
|   |       |   |       test_collections.py
|   |       |   |       test_colorbar.py
|   |       |   |       test_colors.py
|   |       |   |       test_compare_images.py
|   |       |   |       test_constrainedlayout.py
|   |       |   |       test_container.py
|   |       |   |       test_contour.py
|   |       |   |       test_cycles.py
|   |       |   |       test_dates.py
|   |       |   |       test_datetime.py
|   |       |   |       test_determinism.py
|   |       |   |       test_doc.py
|   |       |   |       test_dviread.py
|   |       |   |       test_figure.py
|   |       |   |       test_fontconfig_pattern.py
|   |       |   |       test_font_manager.py
|   |       |   |       test_ft2font.py
|   |       |   |       test_getattr.py
|   |       |   |       test_gridspec.py
|   |       |   |       test_image.py
|   |       |   |       test_legend.py
|   |       |   |       test_lines.py
|   |       |   |       test_marker.py
|   |       |   |       test_mathtext.py
|   |       |   |       test_matplotlib.py
|   |       |   |       test_mlab.py
|   |       |   |       test_multivariate_colormaps.py
|   |       |   |       test_offsetbox.py
|   |       |   |       test_patches.py
|   |       |   |       test_path.py
|   |       |   |       test_patheffects.py
|   |       |   |       test_pickle.py
|   |       |   |       test_png.py
|   |       |   |       test_polar.py
|   |       |   |       test_preprocess_data.py
|   |       |   |       test_pyplot.py
|   |       |   |       test_quiver.py
|   |       |   |       test_rcparams.py
|   |       |   |       test_sankey.py
|   |       |   |       test_scale.py
|   |       |   |       test_simplification.py
|   |       |   |       test_skew.py
|   |       |   |       test_sphinxext.py
|   |       |   |       test_spines.py
|   |       |   |       test_streamplot.py
|   |       |   |       test_style.py
|   |       |   |       test_subplots.py
|   |       |   |       test_table.py
|   |       |   |       test_testing.py
|   |       |   |       test_texmanager.py
|   |       |   |       test_text.py
|   |       |   |       test_textpath.py
|   |       |   |       test_ticker.py
|   |       |   |       test_tightlayout.py
|   |       |   |       test_transforms.py
|   |       |   |       test_triangulation.py
|   |       |   |       test_type1font.py
|   |       |   |       test_units.py
|   |       |   |       test_usetex.py
|   |       |   |       test_widgets.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---tri
|   |       |   |   |   _triangulation.py
|   |       |   |   |   _triangulation.pyi
|   |       |   |   |   _tricontour.py
|   |       |   |   |   _tricontour.pyi
|   |       |   |   |   _trifinder.py
|   |       |   |   |   _trifinder.pyi
|   |       |   |   |   _triinterpolate.py
|   |       |   |   |   _triinterpolate.pyi
|   |       |   |   |   _tripcolor.py
|   |       |   |   |   _tripcolor.pyi
|   |       |   |   |   _triplot.py
|   |       |   |   |   _triplot.pyi
|   |       |   |   |   _trirefine.py
|   |       |   |   |   _trirefine.pyi
|   |       |   |   |   _tritools.py
|   |       |   |   |   _tritools.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _triangulation.cpython-312.pyc
|   |       |   |           _tricontour.cpython-312.pyc
|   |       |   |           _trifinder.cpython-312.pyc
|   |       |   |           _triinterpolate.cpython-312.pyc
|   |       |   |           _tripcolor.cpython-312.pyc
|   |       |   |           _triplot.cpython-312.pyc
|   |       |   |           _trirefine.cpython-312.pyc
|   |       |   |           _tritools.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---_api
|   |       |   |   |   deprecation.py
|   |       |   |   |   deprecation.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           deprecation.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           artist.cpython-312.pyc
|   |       |           axis.cpython-312.pyc
|   |       |           backend_bases.cpython-312.pyc
|   |       |           backend_managers.cpython-312.pyc
|   |       |           backend_tools.cpython-312.pyc
|   |       |           bezier.cpython-312.pyc
|   |       |           category.cpython-312.pyc
|   |       |           cbook.cpython-312.pyc
|   |       |           cm.cpython-312.pyc
|   |       |           collections.cpython-312.pyc
|   |       |           colorbar.cpython-312.pyc
|   |       |           colorizer.cpython-312.pyc
|   |       |           colors.cpython-312.pyc
|   |       |           container.cpython-312.pyc
|   |       |           contour.cpython-312.pyc
|   |       |           dates.cpython-312.pyc
|   |       |           dviread.cpython-312.pyc
|   |       |           figure.cpython-312.pyc
|   |       |           font_manager.cpython-312.pyc
|   |       |           gridspec.cpython-312.pyc
|   |       |           hatch.cpython-312.pyc
|   |       |           image.cpython-312.pyc
|   |       |           inset.cpython-312.pyc
|   |       |           layout_engine.cpython-312.pyc
|   |       |           legend.cpython-312.pyc
|   |       |           legend_handler.cpython-312.pyc
|   |       |           lines.cpython-312.pyc
|   |       |           markers.cpython-312.pyc
|   |       |           mathtext.cpython-312.pyc
|   |       |           mlab.cpython-312.pyc
|   |       |           offsetbox.cpython-312.pyc
|   |       |           patches.cpython-312.pyc
|   |       |           path.cpython-312.pyc
|   |       |           pyplot.cpython-312.pyc
|   |       |           quiver.cpython-312.pyc
|   |       |           rcsetup.cpython-312.pyc
|   |       |           scale.cpython-312.pyc
|   |       |           spines.cpython-312.pyc
|   |       |           stackplot.cpython-312.pyc
|   |       |           streamplot.cpython-312.pyc
|   |       |           table.cpython-312.pyc
|   |       |           texmanager.cpython-312.pyc
|   |       |           text.cpython-312.pyc
|   |       |           textpath.cpython-312.pyc
|   |       |           ticker.cpython-312.pyc
|   |       |           transforms.cpython-312.pyc
|   |       |           units.cpython-312.pyc
|   |       |           widgets.cpython-312.pyc
|   |       |           _afm.cpython-312.pyc
|   |       |           _blocking_input.cpython-312.pyc
|   |       |           _cm.cpython-312.pyc
|   |       |           _cm_bivar.cpython-312.pyc
|   |       |           _cm_listed.cpython-312.pyc
|   |       |           _cm_multivar.cpython-312.pyc
|   |       |           _color_data.cpython-312.pyc
|   |       |           _constrained_layout.cpython-312.pyc
|   |       |           _docstring.cpython-312.pyc
|   |       |           _enums.cpython-312.pyc
|   |       |           _fontconfig_pattern.cpython-312.pyc
|   |       |           _layoutgrid.cpython-312.pyc
|   |       |           _mathtext.cpython-312.pyc
|   |       |           _mathtext_data.cpython-312.pyc
|   |       |           _pylab_helpers.cpython-312.pyc
|   |       |           _text_helpers.cpython-312.pyc
|   |       |           _tight_bbox.cpython-312.pyc
|   |       |           _tight_layout.cpython-312.pyc
|   |       |           _version.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---matplotlib-3.10.6.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---mpl_toolkits
|   |       |   +---axes_grid1
|   |       |   |   |   anchored_artists.py
|   |       |   |   |   axes_divider.py
|   |       |   |   |   axes_grid.py
|   |       |   |   |   axes_rgb.py
|   |       |   |   |   axes_size.py
|   |       |   |   |   inset_locator.py
|   |       |   |   |   mpl_axes.py
|   |       |   |   |   parasite_axes.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---tests
|   |       |   |           conftest.py
|   |       |   |           test_axes_grid1.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---axisartist
|   |       |   |   |   angle_helper.py
|   |       |   |   |   axes_divider.py
|   |       |   |   |   axislines.py
|   |       |   |   |   axisline_style.py
|   |       |   |   |   axis_artist.py
|   |       |   |   |   floating_axes.py
|   |       |   |   |   grid_finder.py
|   |       |   |   |   grid_helper_curvelinear.py
|   |       |   |   |   parasite_axes.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---tests
|   |       |   |           conftest.py
|   |       |   |           test_angle_helper.py
|   |       |   |           test_axislines.py
|   |       |   |           test_axis_artist.py
|   |       |   |           test_floating_axes.py
|   |       |   |           test_grid_finder.py
|   |       |   |           test_grid_helper_curvelinear.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   \---mplot3d
|   |       |       |   art3d.py
|   |       |       |   axes3d.py
|   |       |       |   axis3d.py
|   |       |       |   proj3d.py
|   |       |       |   __init__.py
|   |       |       |   
|   |       |       +---tests
|   |       |       |       conftest.py
|   |       |       |       test_art3d.py
|   |       |       |       test_axes3d.py
|   |       |       |       test_legend3d.py
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       \---__pycache__
|   |       |               art3d.cpython-312.pyc
|   |       |               axes3d.cpython-312.pyc
|   |       |               axis3d.cpython-312.pyc
|   |       |               proj3d.cpython-312.pyc
|   |       |               __init__.cpython-312.pyc
|   |       |               
|   |       +---numpy
|   |       |   |   conftest.py
|   |       |   |   dtypes.py
|   |       |   |   dtypes.pyi
|   |       |   |   exceptions.py
|   |       |   |   exceptions.pyi
|   |       |   |   matlib.py
|   |       |   |   matlib.pyi
|   |       |   |   py.typed
|   |       |   |   version.py
|   |       |   |   version.pyi
|   |       |   |   _array_api_info.py
|   |       |   |   _array_api_info.pyi
|   |       |   |   _configtool.py
|   |       |   |   _configtool.pyi
|   |       |   |   _distributor_init.py
|   |       |   |   _distributor_init.pyi
|   |       |   |   _expired_attrs_2_0.py
|   |       |   |   _expired_attrs_2_0.pyi
|   |       |   |   _globals.py
|   |       |   |   _globals.pyi
|   |       |   |   _pytesttester.py
|   |       |   |   _pytesttester.pyi
|   |       |   |   __config__.py
|   |       |   |   __config__.pyi
|   |       |   |   __init__.cython-30.pxd
|   |       |   |   __init__.pxd
|   |       |   |   __init__.py
|   |       |   |   __init__.pyi
|   |       |   |   
|   |       |   +---char
|   |       |   |       __init__.py
|   |       |   |       __init__.pyi
|   |       |   |       
|   |       |   +---core
|   |       |   |       arrayprint.py
|   |       |   |       defchararray.py
|   |       |   |       einsumfunc.py
|   |       |   |       fromnumeric.py
|   |       |   |       function_base.py
|   |       |   |       getlimits.py
|   |       |   |       multiarray.py
|   |       |   |       numeric.py
|   |       |   |       numerictypes.py
|   |       |   |       overrides.py
|   |       |   |       overrides.pyi
|   |       |   |       records.py
|   |       |   |       shape_base.py
|   |       |   |       umath.py
|   |       |   |       _dtype.py
|   |       |   |       _dtype.pyi
|   |       |   |       _dtype_ctypes.py
|   |       |   |       _dtype_ctypes.pyi
|   |       |   |       _internal.py
|   |       |   |       _multiarray_umath.py
|   |       |   |       _utils.py
|   |       |   |       __init__.py
|   |       |   |       __init__.pyi
|   |       |   |       
|   |       |   +---ctypeslib
|   |       |   |       _ctypeslib.py
|   |       |   |       _ctypeslib.pyi
|   |       |   |       __init__.py
|   |       |   |       __init__.pyi
|   |       |   |       
|   |       |   +---doc
|   |       |   |       ufuncs.py
|   |       |   |       
|   |       |   +---f2py
|   |       |   |   |   auxfuncs.py
|   |       |   |   |   auxfuncs.pyi
|   |       |   |   |   capi_maps.py
|   |       |   |   |   capi_maps.pyi
|   |       |   |   |   cb_rules.py
|   |       |   |   |   cb_rules.pyi
|   |       |   |   |   cfuncs.py
|   |       |   |   |   cfuncs.pyi
|   |       |   |   |   common_rules.py
|   |       |   |   |   common_rules.pyi
|   |       |   |   |   crackfortran.py
|   |       |   |   |   crackfortran.pyi
|   |       |   |   |   diagnose.py
|   |       |   |   |   diagnose.pyi
|   |       |   |   |   f2py2e.py
|   |       |   |   |   f2py2e.pyi
|   |       |   |   |   f90mod_rules.py
|   |       |   |   |   f90mod_rules.pyi
|   |       |   |   |   func2subr.py
|   |       |   |   |   func2subr.pyi
|   |       |   |   |   rules.py
|   |       |   |   |   rules.pyi
|   |       |   |   |   setup.cfg
|   |       |   |   |   symbolic.py
|   |       |   |   |   symbolic.pyi
|   |       |   |   |   use_rules.py
|   |       |   |   |   use_rules.pyi
|   |       |   |   |   _isocbind.py
|   |       |   |   |   _isocbind.pyi
|   |       |   |   |   _src_pyf.py
|   |       |   |   |   _src_pyf.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   __main__.py
|   |       |   |   |   __version__.py
|   |       |   |   |   __version__.pyi
|   |       |   |   |   
|   |       |   |   +---src
|   |       |   |   |       fortranobject.c
|   |       |   |   |       fortranobject.h
|   |       |   |   |       
|   |       |   |   +---tests
|   |       |   |   |   |   test_abstract_interface.py
|   |       |   |   |   |   test_array_from_pyobj.py
|   |       |   |   |   |   test_assumed_shape.py
|   |       |   |   |   |   test_block_docstring.py
|   |       |   |   |   |   test_callback.py
|   |       |   |   |   |   test_character.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_crackfortran.py
|   |       |   |   |   |   test_data.py
|   |       |   |   |   |   test_docs.py
|   |       |   |   |   |   test_f2cmap.py
|   |       |   |   |   |   test_f2py2e.py
|   |       |   |   |   |   test_isoc.py
|   |       |   |   |   |   test_kind.py
|   |       |   |   |   |   test_mixed.py
|   |       |   |   |   |   test_modules.py
|   |       |   |   |   |   test_parameter.py
|   |       |   |   |   |   test_pyf_src.py
|   |       |   |   |   |   test_quoted_character.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_return_character.py
|   |       |   |   |   |   test_return_complex.py
|   |       |   |   |   |   test_return_integer.py
|   |       |   |   |   |   test_return_logical.py
|   |       |   |   |   |   test_return_real.py
|   |       |   |   |   |   test_routines.py
|   |       |   |   |   |   test_semicolon_split.py
|   |       |   |   |   |   test_size.py
|   |       |   |   |   |   test_string.py
|   |       |   |   |   |   test_symbolic.py
|   |       |   |   |   |   test_value_attrspec.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---src
|   |       |   |   |       +---abstract_interface
|   |       |   |   |       |       foo.f90
|   |       |   |   |       |       gh18403_mod.f90
|   |       |   |   |       |       
|   |       |   |   |       +---array_from_pyobj
|   |       |   |   |       |       wrapmodule.c
|   |       |   |   |       |       
|   |       |   |   |       +---assumed_shape
|   |       |   |   |       |       .f2py_f2cmap
|   |       |   |   |       |       foo_free.f90
|   |       |   |   |       |       foo_mod.f90
|   |       |   |   |       |       foo_use.f90
|   |       |   |   |       |       precision.f90
|   |       |   |   |       |       
|   |       |   |   |       +---block_docstring
|   |       |   |   |       |       foo.f
|   |       |   |   |       |       
|   |       |   |   |       +---callback
|   |       |   |   |       |       foo.f
|   |       |   |   |       |       gh17797.f90
|   |       |   |   |       |       gh18335.f90
|   |       |   |   |       |       gh25211.f
|   |       |   |   |       |       gh25211.pyf
|   |       |   |   |       |       gh26681.f90
|   |       |   |   |       |       
|   |       |   |   |       +---cli
|   |       |   |   |       |       gh_22819.pyf
|   |       |   |   |       |       hi77.f
|   |       |   |   |       |       hiworld.f90
|   |       |   |   |       |       
|   |       |   |   |       +---common
|   |       |   |   |       |       block.f
|   |       |   |   |       |       gh19161.f90
|   |       |   |   |       |       
|   |       |   |   |       +---crackfortran
|   |       |   |   |       |       accesstype.f90
|   |       |   |   |       |       common_with_division.f
|   |       |   |   |       |       data_common.f
|   |       |   |   |       |       data_multiplier.f
|   |       |   |   |       |       data_stmts.f90
|   |       |   |   |       |       data_with_comments.f
|   |       |   |   |       |       foo_deps.f90
|   |       |   |   |       |       gh15035.f
|   |       |   |   |       |       gh17859.f
|   |       |   |   |       |       gh22648.pyf
|   |       |   |   |       |       gh23533.f
|   |       |   |   |       |       gh23598.f90
|   |       |   |   |       |       gh23598Warn.f90
|   |       |   |   |       |       gh23879.f90
|   |       |   |   |       |       gh27697.f90
|   |       |   |   |       |       gh2848.f90
|   |       |   |   |       |       operators.f90
|   |       |   |   |       |       privatemod.f90
|   |       |   |   |       |       publicmod.f90
|   |       |   |   |       |       pubprivmod.f90
|   |       |   |   |       |       unicode_comment.f90
|   |       |   |   |       |       
|   |       |   |   |       +---f2cmap
|   |       |   |   |       |       .f2py_f2cmap
|   |       |   |   |       |       isoFortranEnvMap.f90
|   |       |   |   |       |       
|   |       |   |   |       +---isocintrin
|   |       |   |   |       |       isoCtests.f90
|   |       |   |   |       |       
|   |       |   |   |       +---kind
|   |       |   |   |       |       foo.f90
|   |       |   |   |       |       
|   |       |   |   |       +---mixed
|   |       |   |   |       |       foo.f
|   |       |   |   |       |       foo_fixed.f90
|   |       |   |   |       |       foo_free.f90
|   |       |   |   |       |       
|   |       |   |   |       +---modules
|   |       |   |   |       |   |   module_data_docstring.f90
|   |       |   |   |       |   |   use_modules.f90
|   |       |   |   |       |   |   
|   |       |   |   |       |   +---gh25337
|   |       |   |   |       |   |       data.f90
|   |       |   |   |       |   |       use_data.f90
|   |       |   |   |       |   |       
|   |       |   |   |       |   \---gh26920
|   |       |   |   |       |           two_mods_with_no_public_entities.f90
|   |       |   |   |       |           two_mods_with_one_public_routine.f90
|   |       |   |   |       |           
|   |       |   |   |       +---negative_bounds
|   |       |   |   |       |       issue_20853.f90
|   |       |   |   |       |       
|   |       |   |   |       +---parameter
|   |       |   |   |       |       constant_array.f90
|   |       |   |   |       |       constant_both.f90
|   |       |   |   |       |       constant_compound.f90
|   |       |   |   |       |       constant_integer.f90
|   |       |   |   |       |       constant_non_compound.f90
|   |       |   |   |       |       constant_real.f90
|   |       |   |   |       |       
|   |       |   |   |       +---quoted_character
|   |       |   |   |       |       foo.f
|   |       |   |   |       |       
|   |       |   |   |       +---regression
|   |       |   |   |       |       AB.inc
|   |       |   |   |       |       assignOnlyModule.f90
|   |       |   |   |       |       datonly.f90
|   |       |   |   |       |       f77comments.f
|   |       |   |   |       |       f77fixedform.f95
|   |       |   |   |       |       f90continuation.f90
|   |       |   |   |       |       incfile.f90
|   |       |   |   |       |       inout.f90
|   |       |   |   |       |       lower_f2py_fortran.f90
|   |       |   |   |       |       mod_derived_types.f90
|   |       |   |   |       |       
|   |       |   |   |       +---return_character
|   |       |   |   |       |       foo77.f
|   |       |   |   |       |       foo90.f90
|   |       |   |   |       |       
|   |       |   |   |       +---return_complex
|   |       |   |   |       |       foo77.f
|   |       |   |   |       |       foo90.f90
|   |       |   |   |       |       
|   |       |   |   |       +---return_integer
|   |       |   |   |       |       foo77.f
|   |       |   |   |       |       foo90.f90
|   |       |   |   |       |       
|   |       |   |   |       +---return_logical
|   |       |   |   |       |       foo77.f
|   |       |   |   |       |       foo90.f90
|   |       |   |   |       |       
|   |       |   |   |       +---return_real
|   |       |   |   |       |       foo77.f
|   |       |   |   |       |       foo90.f90
|   |       |   |   |       |       
|   |       |   |   |       +---routines
|   |       |   |   |       |       funcfortranname.f
|   |       |   |   |       |       funcfortranname.pyf
|   |       |   |   |       |       subrout.f
|   |       |   |   |       |       subrout.pyf
|   |       |   |   |       |       
|   |       |   |   |       +---size
|   |       |   |   |       |       foo.f90
|   |       |   |   |       |       
|   |       |   |   |       +---string
|   |       |   |   |       |       char.f90
|   |       |   |   |       |       fixed_string.f90
|   |       |   |   |       |       gh24008.f
|   |       |   |   |       |       gh24662.f90
|   |       |   |   |       |       gh25286.f90
|   |       |   |   |       |       gh25286.pyf
|   |       |   |   |       |       gh25286_bc.pyf
|   |       |   |   |       |       scalar_string.f90
|   |       |   |   |       |       string.f
|   |       |   |   |       |       
|   |       |   |   |       \---value_attrspec
|   |       |   |   |               gh21665.f90
|   |       |   |   |               
|   |       |   |   \---_backends
|   |       |   |           meson.build.template
|   |       |   |           _backend.py
|   |       |   |           _backend.pyi
|   |       |   |           _distutils.py
|   |       |   |           _distutils.pyi
|   |       |   |           _meson.py
|   |       |   |           _meson.pyi
|   |       |   |           __init__.py
|   |       |   |           __init__.pyi
|   |       |   |           
|   |       |   +---fft
|   |       |   |   |   helper.py
|   |       |   |   |   helper.pyi
|   |       |   |   |   _helper.py
|   |       |   |   |   _helper.pyi
|   |       |   |   |   _pocketfft.py
|   |       |   |   |   _pocketfft.pyi
|   |       |   |   |   _pocketfft_umath.cp312-win_amd64.lib
|   |       |   |   |   _pocketfft_umath.cp312-win_amd64.pyd
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---tests
|   |       |   |           test_helper.py
|   |       |   |           test_pocketfft.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---lib
|   |       |   |   |   array_utils.py
|   |       |   |   |   array_utils.pyi
|   |       |   |   |   format.py
|   |       |   |   |   format.pyi
|   |       |   |   |   introspect.py
|   |       |   |   |   introspect.pyi
|   |       |   |   |   mixins.py
|   |       |   |   |   mixins.pyi
|   |       |   |   |   npyio.py
|   |       |   |   |   npyio.pyi
|   |       |   |   |   recfunctions.py
|   |       |   |   |   recfunctions.pyi
|   |       |   |   |   scimath.py
|   |       |   |   |   scimath.pyi
|   |       |   |   |   stride_tricks.py
|   |       |   |   |   stride_tricks.pyi
|   |       |   |   |   user_array.py
|   |       |   |   |   user_array.pyi
|   |       |   |   |   _arraypad_impl.py
|   |       |   |   |   _arraypad_impl.pyi
|   |       |   |   |   _arraysetops_impl.py
|   |       |   |   |   _arraysetops_impl.pyi
|   |       |   |   |   _arrayterator_impl.py
|   |       |   |   |   _arrayterator_impl.pyi
|   |       |   |   |   _array_utils_impl.py
|   |       |   |   |   _array_utils_impl.pyi
|   |       |   |   |   _datasource.py
|   |       |   |   |   _datasource.pyi
|   |       |   |   |   _format_impl.py
|   |       |   |   |   _format_impl.pyi
|   |       |   |   |   _function_base_impl.py
|   |       |   |   |   _function_base_impl.pyi
|   |       |   |   |   _histograms_impl.py
|   |       |   |   |   _histograms_impl.pyi
|   |       |   |   |   _index_tricks_impl.py
|   |       |   |   |   _index_tricks_impl.pyi
|   |       |   |   |   _iotools.py
|   |       |   |   |   _iotools.pyi
|   |       |   |   |   _nanfunctions_impl.py
|   |       |   |   |   _nanfunctions_impl.pyi
|   |       |   |   |   _npyio_impl.py
|   |       |   |   |   _npyio_impl.pyi
|   |       |   |   |   _polynomial_impl.py
|   |       |   |   |   _polynomial_impl.pyi
|   |       |   |   |   _scimath_impl.py
|   |       |   |   |   _scimath_impl.pyi
|   |       |   |   |   _shape_base_impl.py
|   |       |   |   |   _shape_base_impl.pyi
|   |       |   |   |   _stride_tricks_impl.py
|   |       |   |   |   _stride_tricks_impl.pyi
|   |       |   |   |   _twodim_base_impl.py
|   |       |   |   |   _twodim_base_impl.pyi
|   |       |   |   |   _type_check_impl.py
|   |       |   |   |   _type_check_impl.pyi
|   |       |   |   |   _ufunclike_impl.py
|   |       |   |   |   _ufunclike_impl.pyi
|   |       |   |   |   _user_array_impl.py
|   |       |   |   |   _user_array_impl.pyi
|   |       |   |   |   _utils_impl.py
|   |       |   |   |   _utils_impl.pyi
|   |       |   |   |   _version.py
|   |       |   |   |   _version.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_arraypad.py
|   |       |   |   |   |   test_arraysetops.py
|   |       |   |   |   |   test_arrayterator.py
|   |       |   |   |   |   test_array_utils.py
|   |       |   |   |   |   test_format.py
|   |       |   |   |   |   test_function_base.py
|   |       |   |   |   |   test_histograms.py
|   |       |   |   |   |   test_index_tricks.py
|   |       |   |   |   |   test_io.py
|   |       |   |   |   |   test_loadtxt.py
|   |       |   |   |   |   test_mixins.py
|   |       |   |   |   |   test_nanfunctions.py
|   |       |   |   |   |   test_packbits.py
|   |       |   |   |   |   test_polynomial.py
|   |       |   |   |   |   test_recfunctions.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_shape_base.py
|   |       |   |   |   |   test_stride_tricks.py
|   |       |   |   |   |   test_twodim_base.py
|   |       |   |   |   |   test_type_check.py
|   |       |   |   |   |   test_ufunclike.py
|   |       |   |   |   |   test_utils.py
|   |       |   |   |   |   test__datasource.py
|   |       |   |   |   |   test__iotools.py
|   |       |   |   |   |   test__version.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---data
|   |       |   |   |           py2-np0-objarr.npy
|   |       |   |   |           py2-objarr.npy
|   |       |   |   |           py2-objarr.npz
|   |       |   |   |           py3-objarr.npy
|   |       |   |   |           py3-objarr.npz
|   |       |   |   |           python3.npy
|   |       |   |   |           win64python2.npy
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           array_utils.cpython-312.pyc
|   |       |   |           format.cpython-312.pyc
|   |       |   |           introspect.cpython-312.pyc
|   |       |   |           mixins.cpython-312.pyc
|   |       |   |           npyio.cpython-312.pyc
|   |       |   |           scimath.cpython-312.pyc
|   |       |   |           stride_tricks.cpython-312.pyc
|   |       |   |           _arraypad_impl.cpython-312.pyc
|   |       |   |           _arraysetops_impl.cpython-312.pyc
|   |       |   |           _arrayterator_impl.cpython-312.pyc
|   |       |   |           _array_utils_impl.cpython-312.pyc
|   |       |   |           _datasource.cpython-312.pyc
|   |       |   |           _format_impl.cpython-312.pyc
|   |       |   |           _function_base_impl.cpython-312.pyc
|   |       |   |           _histograms_impl.cpython-312.pyc
|   |       |   |           _index_tricks_impl.cpython-312.pyc
|   |       |   |           _iotools.cpython-312.pyc
|   |       |   |           _nanfunctions_impl.cpython-312.pyc
|   |       |   |           _npyio_impl.cpython-312.pyc
|   |       |   |           _polynomial_impl.cpython-312.pyc
|   |       |   |           _scimath_impl.cpython-312.pyc
|   |       |   |           _shape_base_impl.cpython-312.pyc
|   |       |   |           _stride_tricks_impl.cpython-312.pyc
|   |       |   |           _twodim_base_impl.cpython-312.pyc
|   |       |   |           _type_check_impl.cpython-312.pyc
|   |       |   |           _ufunclike_impl.cpython-312.pyc
|   |       |   |           _utils_impl.cpython-312.pyc
|   |       |   |           _version.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---linalg
|   |       |   |   |   lapack_lite.cp312-win_amd64.lib
|   |       |   |   |   lapack_lite.cp312-win_amd64.pyd
|   |       |   |   |   lapack_lite.pyi
|   |       |   |   |   linalg.py
|   |       |   |   |   linalg.pyi
|   |       |   |   |   _linalg.py
|   |       |   |   |   _linalg.pyi
|   |       |   |   |   _umath_linalg.cp312-win_amd64.lib
|   |       |   |   |   _umath_linalg.cp312-win_amd64.pyd
|   |       |   |   |   _umath_linalg.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |       test_deprecations.py
|   |       |   |   |       test_linalg.py
|   |       |   |   |       test_regression.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---__pycache__
|   |       |   |           linalg.cpython-312.pyc
|   |       |   |           _linalg.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---ma
|   |       |   |   |   API_CHANGES.txt
|   |       |   |   |   core.py
|   |       |   |   |   core.pyi
|   |       |   |   |   extras.py
|   |       |   |   |   extras.pyi
|   |       |   |   |   LICENSE
|   |       |   |   |   mrecords.py
|   |       |   |   |   mrecords.pyi
|   |       |   |   |   README.rst
|   |       |   |   |   testutils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |       test_arrayobject.py
|   |       |   |   |       test_core.py
|   |       |   |   |       test_deprecations.py
|   |       |   |   |       test_extras.py
|   |       |   |   |       test_mrecords.py
|   |       |   |   |       test_old_ma.py
|   |       |   |   |       test_regression.py
|   |       |   |   |       test_subclassing.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---__pycache__
|   |       |   |           core.cpython-312.pyc
|   |       |   |           extras.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---matrixlib
|   |       |   |   |   defmatrix.py
|   |       |   |   |   defmatrix.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |       test_defmatrix.py
|   |       |   |   |       test_interaction.py
|   |       |   |   |       test_masked_matrix.py
|   |       |   |   |       test_matrix_linalg.py
|   |       |   |   |       test_multiarray.py
|   |       |   |   |       test_numeric.py
|   |       |   |   |       test_regression.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---__pycache__
|   |       |   |           defmatrix.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---polynomial
|   |       |   |   |   chebyshev.py
|   |       |   |   |   chebyshev.pyi
|   |       |   |   |   hermite.py
|   |       |   |   |   hermite.pyi
|   |       |   |   |   hermite_e.py
|   |       |   |   |   hermite_e.pyi
|   |       |   |   |   laguerre.py
|   |       |   |   |   laguerre.pyi
|   |       |   |   |   legendre.py
|   |       |   |   |   legendre.pyi
|   |       |   |   |   polynomial.py
|   |       |   |   |   polynomial.pyi
|   |       |   |   |   polyutils.py
|   |       |   |   |   polyutils.pyi
|   |       |   |   |   _polybase.py
|   |       |   |   |   _polybase.pyi
|   |       |   |   |   _polytypes.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---tests
|   |       |   |           test_chebyshev.py
|   |       |   |           test_classes.py
|   |       |   |           test_hermite.py
|   |       |   |           test_hermite_e.py
|   |       |   |           test_laguerre.py
|   |       |   |           test_legendre.py
|   |       |   |           test_polynomial.py
|   |       |   |           test_polyutils.py
|   |       |   |           test_printing.py
|   |       |   |           test_symbol.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---random
|   |       |   |   |   bit_generator.cp312-win_amd64.lib
|   |       |   |   |   bit_generator.cp312-win_amd64.pyd
|   |       |   |   |   bit_generator.pxd
|   |       |   |   |   bit_generator.pyi
|   |       |   |   |   c_distributions.pxd
|   |       |   |   |   LICENSE.md
|   |       |   |   |   mtrand.cp312-win_amd64.lib
|   |       |   |   |   mtrand.cp312-win_amd64.pyd
|   |       |   |   |   mtrand.pyi
|   |       |   |   |   _bounded_integers.cp312-win_amd64.lib
|   |       |   |   |   _bounded_integers.cp312-win_amd64.pyd
|   |       |   |   |   _bounded_integers.pxd
|   |       |   |   |   _bounded_integers.pyi
|   |       |   |   |   _common.cp312-win_amd64.lib
|   |       |   |   |   _common.cp312-win_amd64.pyd
|   |       |   |   |   _common.pxd
|   |       |   |   |   _common.pyi
|   |       |   |   |   _generator.cp312-win_amd64.lib
|   |       |   |   |   _generator.cp312-win_amd64.pyd
|   |       |   |   |   _generator.pyi
|   |       |   |   |   _mt19937.cp312-win_amd64.lib
|   |       |   |   |   _mt19937.cp312-win_amd64.pyd
|   |       |   |   |   _mt19937.pyi
|   |       |   |   |   _pcg64.cp312-win_amd64.lib
|   |       |   |   |   _pcg64.cp312-win_amd64.pyd
|   |       |   |   |   _pcg64.pyi
|   |       |   |   |   _philox.cp312-win_amd64.lib
|   |       |   |   |   _philox.cp312-win_amd64.pyd
|   |       |   |   |   _philox.pyi
|   |       |   |   |   _pickle.py
|   |       |   |   |   _pickle.pyi
|   |       |   |   |   _sfc64.cp312-win_amd64.lib
|   |       |   |   |   _sfc64.cp312-win_amd64.pyd
|   |       |   |   |   _sfc64.pyi
|   |       |   |   |   __init__.pxd
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---lib
|   |       |   |   |       npyrandom.lib
|   |       |   |   |       
|   |       |   |   +---tests
|   |       |   |   |   |   test_direct.py
|   |       |   |   |   |   test_extending.py
|   |       |   |   |   |   test_generator_mt19937.py
|   |       |   |   |   |   test_generator_mt19937_regressions.py
|   |       |   |   |   |   test_random.py
|   |       |   |   |   |   test_randomstate.py
|   |       |   |   |   |   test_randomstate_regression.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_seed_sequence.py
|   |       |   |   |   |   test_smoke.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---data
|   |       |   |   |           generator_pcg64_np121.pkl.gz
|   |       |   |   |           generator_pcg64_np126.pkl.gz
|   |       |   |   |           mt19937-testset-1.csv
|   |       |   |   |           mt19937-testset-2.csv
|   |       |   |   |           pcg64-testset-1.csv
|   |       |   |   |           pcg64-testset-2.csv
|   |       |   |   |           pcg64dxsm-testset-1.csv
|   |       |   |   |           pcg64dxsm-testset-2.csv
|   |       |   |   |           philox-testset-1.csv
|   |       |   |   |           philox-testset-2.csv
|   |       |   |   |           sfc64-testset-1.csv
|   |       |   |   |           sfc64-testset-2.csv
|   |       |   |   |           sfc64_np126.pkl.gz
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---_examples
|   |       |   |   |   +---cffi
|   |       |   |   |   |       extending.py
|   |       |   |   |   |       parse.py
|   |       |   |   |   |       
|   |       |   |   |   +---cython
|   |       |   |   |   |       extending.pyx
|   |       |   |   |   |       extending_distributions.pyx
|   |       |   |   |   |       meson.build
|   |       |   |   |   |       
|   |       |   |   |   \---numba
|   |       |   |   |           extending.py
|   |       |   |   |           extending_distributions.py
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           _pickle.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---rec
|   |       |   |       __init__.py
|   |       |   |       __init__.pyi
|   |       |   |       
|   |       |   +---strings
|   |       |   |       __init__.py
|   |       |   |       __init__.pyi
|   |       |   |       
|   |       |   +---testing
|   |       |   |   |   overrides.py
|   |       |   |   |   overrides.pyi
|   |       |   |   |   print_coercion_tables.py
|   |       |   |   |   print_coercion_tables.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |       test_utils.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---_private
|   |       |   |           extbuild.py
|   |       |   |           extbuild.pyi
|   |       |   |           utils.py
|   |       |   |           utils.pyi
|   |       |   |           __init__.py
|   |       |   |           __init__.pyi
|   |       |   |           
|   |       |   +---tests
|   |       |   |       test_configtool.py
|   |       |   |       test_ctypeslib.py
|   |       |   |       test_lazyloading.py
|   |       |   |       test_matlib.py
|   |       |   |       test_numpy_config.py
|   |       |   |       test_numpy_version.py
|   |       |   |       test_public_api.py
|   |       |   |       test_reloading.py
|   |       |   |       test_scripts.py
|   |       |   |       test_warnings.py
|   |       |   |       test__all__.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---typing
|   |       |   |   |   mypy_plugin.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---tests
|   |       |   |       |   test_isfile.py
|   |       |   |       |   test_runtime.py
|   |       |   |       |   test_typing.py
|   |       |   |       |   __init__.py
|   |       |   |       |   
|   |       |   |       \---data
|   |       |   |           |   mypy.ini
|   |       |   |           |   
|   |       |   |           +---fail
|   |       |   |           |       arithmetic.pyi
|   |       |   |           |       arrayprint.pyi
|   |       |   |           |       arrayterator.pyi
|   |       |   |           |       array_constructors.pyi
|   |       |   |           |       array_like.pyi
|   |       |   |           |       array_pad.pyi
|   |       |   |           |       bitwise_ops.pyi
|   |       |   |           |       char.pyi
|   |       |   |           |       chararray.pyi
|   |       |   |           |       comparisons.pyi
|   |       |   |           |       constants.pyi
|   |       |   |           |       datasource.pyi
|   |       |   |           |       dtype.pyi
|   |       |   |           |       einsumfunc.pyi
|   |       |   |           |       flatiter.pyi
|   |       |   |           |       fromnumeric.pyi
|   |       |   |           |       histograms.pyi
|   |       |   |           |       index_tricks.pyi
|   |       |   |           |       lib_function_base.pyi
|   |       |   |           |       lib_polynomial.pyi
|   |       |   |           |       lib_utils.pyi
|   |       |   |           |       lib_version.pyi
|   |       |   |           |       linalg.pyi
|   |       |   |           |       ma.pyi
|   |       |   |           |       memmap.pyi
|   |       |   |           |       modules.pyi
|   |       |   |           |       multiarray.pyi
|   |       |   |           |       ndarray.pyi
|   |       |   |           |       ndarray_misc.pyi
|   |       |   |           |       nditer.pyi
|   |       |   |           |       nested_sequence.pyi
|   |       |   |           |       npyio.pyi
|   |       |   |           |       numerictypes.pyi
|   |       |   |           |       random.pyi
|   |       |   |           |       rec.pyi
|   |       |   |           |       scalars.pyi
|   |       |   |           |       shape.pyi
|   |       |   |           |       shape_base.pyi
|   |       |   |           |       stride_tricks.pyi
|   |       |   |           |       strings.pyi
|   |       |   |           |       testing.pyi
|   |       |   |           |       twodim_base.pyi
|   |       |   |           |       type_check.pyi
|   |       |   |           |       ufunclike.pyi
|   |       |   |           |       ufuncs.pyi
|   |       |   |           |       ufunc_config.pyi
|   |       |   |           |       warnings_and_errors.pyi
|   |       |   |           |       
|   |       |   |           +---misc
|   |       |   |           |       extended_precision.pyi
|   |       |   |           |       
|   |       |   |           +---pass
|   |       |   |           |       arithmetic.py
|   |       |   |           |       arrayprint.py
|   |       |   |           |       arrayterator.py
|   |       |   |           |       array_constructors.py
|   |       |   |           |       array_like.py
|   |       |   |           |       bitwise_ops.py
|   |       |   |           |       comparisons.py
|   |       |   |           |       dtype.py
|   |       |   |           |       einsumfunc.py
|   |       |   |           |       flatiter.py
|   |       |   |           |       fromnumeric.py
|   |       |   |           |       index_tricks.py
|   |       |   |           |       lib_user_array.py
|   |       |   |           |       lib_utils.py
|   |       |   |           |       lib_version.py
|   |       |   |           |       literal.py
|   |       |   |           |       ma.py
|   |       |   |           |       mod.py
|   |       |   |           |       modules.py
|   |       |   |           |       multiarray.py
|   |       |   |           |       ndarray_conversion.py
|   |       |   |           |       ndarray_misc.py
|   |       |   |           |       ndarray_shape_manipulation.py
|   |       |   |           |       nditer.py
|   |       |   |           |       numeric.py
|   |       |   |           |       numerictypes.py
|   |       |   |           |       random.py
|   |       |   |           |       recfunctions.py
|   |       |   |           |       scalars.py
|   |       |   |           |       shape.py
|   |       |   |           |       simple.py
|   |       |   |           |       simple_py3.py
|   |       |   |           |       ufunclike.py
|   |       |   |           |       ufuncs.py
|   |       |   |           |       ufunc_config.py
|   |       |   |           |       warnings_and_errors.py
|   |       |   |           |       
|   |       |   |           \---reveal
|   |       |   |                   arithmetic.pyi
|   |       |   |                   arraypad.pyi
|   |       |   |                   arrayprint.pyi
|   |       |   |                   arraysetops.pyi
|   |       |   |                   arrayterator.pyi
|   |       |   |                   array_api_info.pyi
|   |       |   |                   array_constructors.pyi
|   |       |   |                   bitwise_ops.pyi
|   |       |   |                   char.pyi
|   |       |   |                   chararray.pyi
|   |       |   |                   comparisons.pyi
|   |       |   |                   constants.pyi
|   |       |   |                   ctypeslib.pyi
|   |       |   |                   datasource.pyi
|   |       |   |                   dtype.pyi
|   |       |   |                   einsumfunc.pyi
|   |       |   |                   emath.pyi
|   |       |   |                   fft.pyi
|   |       |   |                   flatiter.pyi
|   |       |   |                   fromnumeric.pyi
|   |       |   |                   getlimits.pyi
|   |       |   |                   histograms.pyi
|   |       |   |                   index_tricks.pyi
|   |       |   |                   lib_function_base.pyi
|   |       |   |                   lib_polynomial.pyi
|   |       |   |                   lib_utils.pyi
|   |       |   |                   lib_version.pyi
|   |       |   |                   linalg.pyi
|   |       |   |                   ma.pyi
|   |       |   |                   matrix.pyi
|   |       |   |                   memmap.pyi
|   |       |   |                   mod.pyi
|   |       |   |                   modules.pyi
|   |       |   |                   multiarray.pyi
|   |       |   |                   nbit_base_example.pyi
|   |       |   |                   ndarray_assignability.pyi
|   |       |   |                   ndarray_conversion.pyi
|   |       |   |                   ndarray_misc.pyi
|   |       |   |                   ndarray_shape_manipulation.pyi
|   |       |   |                   nditer.pyi
|   |       |   |                   nested_sequence.pyi
|   |       |   |                   npyio.pyi
|   |       |   |                   numeric.pyi
|   |       |   |                   numerictypes.pyi
|   |       |   |                   polynomial_polybase.pyi
|   |       |   |                   polynomial_polyutils.pyi
|   |       |   |                   polynomial_series.pyi
|   |       |   |                   random.pyi
|   |       |   |                   rec.pyi
|   |       |   |                   scalars.pyi
|   |       |   |                   shape.pyi
|   |       |   |                   shape_base.pyi
|   |       |   |                   stride_tricks.pyi
|   |       |   |                   strings.pyi
|   |       |   |                   testing.pyi
|   |       |   |                   twodim_base.pyi
|   |       |   |                   type_check.pyi
|   |       |   |                   ufunclike.pyi
|   |       |   |                   ufuncs.pyi
|   |       |   |                   ufunc_config.pyi
|   |       |   |                   warnings_and_errors.pyi
|   |       |   |                   
|   |       |   +---_core
|   |       |   |   |   arrayprint.py
|   |       |   |   |   arrayprint.pyi
|   |       |   |   |   cversions.py
|   |       |   |   |   defchararray.py
|   |       |   |   |   defchararray.pyi
|   |       |   |   |   einsumfunc.py
|   |       |   |   |   einsumfunc.pyi
|   |       |   |   |   fromnumeric.py
|   |       |   |   |   fromnumeric.pyi
|   |       |   |   |   function_base.py
|   |       |   |   |   function_base.pyi
|   |       |   |   |   getlimits.py
|   |       |   |   |   getlimits.pyi
|   |       |   |   |   memmap.py
|   |       |   |   |   memmap.pyi
|   |       |   |   |   multiarray.py
|   |       |   |   |   multiarray.pyi
|   |       |   |   |   numeric.py
|   |       |   |   |   numeric.pyi
|   |       |   |   |   numerictypes.py
|   |       |   |   |   numerictypes.pyi
|   |       |   |   |   overrides.py
|   |       |   |   |   overrides.pyi
|   |       |   |   |   printoptions.py
|   |       |   |   |   printoptions.pyi
|   |       |   |   |   records.py
|   |       |   |   |   records.pyi
|   |       |   |   |   shape_base.py
|   |       |   |   |   shape_base.pyi
|   |       |   |   |   strings.py
|   |       |   |   |   strings.pyi
|   |       |   |   |   umath.py
|   |       |   |   |   umath.pyi
|   |       |   |   |   _add_newdocs.py
|   |       |   |   |   _add_newdocs.pyi
|   |       |   |   |   _add_newdocs_scalars.py
|   |       |   |   |   _add_newdocs_scalars.pyi
|   |       |   |   |   _asarray.py
|   |       |   |   |   _asarray.pyi
|   |       |   |   |   _dtype.py
|   |       |   |   |   _dtype.pyi
|   |       |   |   |   _dtype_ctypes.py
|   |       |   |   |   _dtype_ctypes.pyi
|   |       |   |   |   _exceptions.py
|   |       |   |   |   _exceptions.pyi
|   |       |   |   |   _internal.py
|   |       |   |   |   _internal.pyi
|   |       |   |   |   _machar.py
|   |       |   |   |   _machar.pyi
|   |       |   |   |   _methods.py
|   |       |   |   |   _methods.pyi
|   |       |   |   |   _multiarray_tests.cp312-win_amd64.lib
|   |       |   |   |   _multiarray_tests.cp312-win_amd64.pyd
|   |       |   |   |   _multiarray_umath.cp312-win_amd64.lib
|   |       |   |   |   _multiarray_umath.cp312-win_amd64.pyd
|   |       |   |   |   _operand_flag_tests.cp312-win_amd64.lib
|   |       |   |   |   _operand_flag_tests.cp312-win_amd64.pyd
|   |       |   |   |   _rational_tests.cp312-win_amd64.lib
|   |       |   |   |   _rational_tests.cp312-win_amd64.pyd
|   |       |   |   |   _simd.cp312-win_amd64.lib
|   |       |   |   |   _simd.cp312-win_amd64.pyd
|   |       |   |   |   _simd.pyi
|   |       |   |   |   _string_helpers.py
|   |       |   |   |   _string_helpers.pyi
|   |       |   |   |   _struct_ufunc_tests.cp312-win_amd64.lib
|   |       |   |   |   _struct_ufunc_tests.cp312-win_amd64.pyd
|   |       |   |   |   _type_aliases.py
|   |       |   |   |   _type_aliases.pyi
|   |       |   |   |   _ufunc_config.py
|   |       |   |   |   _ufunc_config.pyi
|   |       |   |   |   _umath_tests.cp312-win_amd64.lib
|   |       |   |   |   _umath_tests.cp312-win_amd64.pyd
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---include
|   |       |   |   |   \---numpy
|   |       |   |   |       |   arrayobject.h
|   |       |   |   |       |   arrayscalars.h
|   |       |   |   |       |   dtype_api.h
|   |       |   |   |       |   halffloat.h
|   |       |   |   |       |   ndarrayobject.h
|   |       |   |   |       |   ndarraytypes.h
|   |       |   |   |       |   npy_2_compat.h
|   |       |   |   |       |   npy_2_complexcompat.h
|   |       |   |   |       |   npy_3kcompat.h
|   |       |   |   |       |   npy_common.h
|   |       |   |   |       |   npy_cpu.h
|   |       |   |   |       |   npy_endian.h
|   |       |   |   |       |   npy_math.h
|   |       |   |   |       |   npy_no_deprecated_api.h
|   |       |   |   |       |   npy_os.h
|   |       |   |   |       |   numpyconfig.h
|   |       |   |   |       |   ufuncobject.h
|   |       |   |   |       |   utils.h
|   |       |   |   |       |   _neighborhood_iterator_imp.h
|   |       |   |   |       |   _numpyconfig.h
|   |       |   |   |       |   _public_dtype_api_table.h
|   |       |   |   |       |   __multiarray_api.c
|   |       |   |   |       |   __multiarray_api.h
|   |       |   |   |       |   __ufunc_api.c
|   |       |   |   |       |   __ufunc_api.h
|   |       |   |   |       |   
|   |       |   |   |       \---random
|   |       |   |   |               bitgen.h
|   |       |   |   |               distributions.h
|   |       |   |   |               libdivide.h
|   |       |   |   |               LICENSE.txt
|   |       |   |   |               
|   |       |   |   +---lib
|   |       |   |   |   |   npymath.lib
|   |       |   |   |   |   
|   |       |   |   |   +---npy-pkg-config
|   |       |   |   |   |       mlib.ini
|   |       |   |   |   |       npymath.ini
|   |       |   |   |   |       
|   |       |   |   |   \---pkgconfig
|   |       |   |   |           numpy.pc
|   |       |   |   |           
|   |       |   |   +---tests
|   |       |   |   |   |   test_abc.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_argparse.py
|   |       |   |   |   |   test_arraymethod.py
|   |       |   |   |   |   test_arrayobject.py
|   |       |   |   |   |   test_arrayprint.py
|   |       |   |   |   |   test_array_api_info.py
|   |       |   |   |   |   test_array_coercion.py
|   |       |   |   |   |   test_array_interface.py
|   |       |   |   |   |   test_casting_floatingpoint_errors.py
|   |       |   |   |   |   test_casting_unittests.py
|   |       |   |   |   |   test_conversion_utils.py
|   |       |   |   |   |   test_cpu_dispatcher.py
|   |       |   |   |   |   test_cpu_features.py
|   |       |   |   |   |   test_custom_dtypes.py
|   |       |   |   |   |   test_cython.py
|   |       |   |   |   |   test_datetime.py
|   |       |   |   |   |   test_defchararray.py
|   |       |   |   |   |   test_deprecations.py
|   |       |   |   |   |   test_dlpack.py
|   |       |   |   |   |   test_dtype.py
|   |       |   |   |   |   test_einsum.py
|   |       |   |   |   |   test_errstate.py
|   |       |   |   |   |   test_extint128.py
|   |       |   |   |   |   test_function_base.py
|   |       |   |   |   |   test_getlimits.py
|   |       |   |   |   |   test_half.py
|   |       |   |   |   |   test_hashtable.py
|   |       |   |   |   |   test_indexerrors.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_item_selection.py
|   |       |   |   |   |   test_limited_api.py
|   |       |   |   |   |   test_longdouble.py
|   |       |   |   |   |   test_machar.py
|   |       |   |   |   |   test_memmap.py
|   |       |   |   |   |   test_mem_overlap.py
|   |       |   |   |   |   test_mem_policy.py
|   |       |   |   |   |   test_multiarray.py
|   |       |   |   |   |   test_multithreading.py
|   |       |   |   |   |   test_nditer.py
|   |       |   |   |   |   test_nep50_promotions.py
|   |       |   |   |   |   test_numeric.py
|   |       |   |   |   |   test_numerictypes.py
|   |       |   |   |   |   test_overrides.py
|   |       |   |   |   |   test_print.py
|   |       |   |   |   |   test_protocols.py
|   |       |   |   |   |   test_records.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_scalarbuffer.py
|   |       |   |   |   |   test_scalarinherit.py
|   |       |   |   |   |   test_scalarmath.py
|   |       |   |   |   |   test_scalarprint.py
|   |       |   |   |   |   test_scalar_ctors.py
|   |       |   |   |   |   test_scalar_methods.py
|   |       |   |   |   |   test_shape_base.py
|   |       |   |   |   |   test_simd.py
|   |       |   |   |   |   test_simd_module.py
|   |       |   |   |   |   test_stringdtype.py
|   |       |   |   |   |   test_strings.py
|   |       |   |   |   |   test_ufunc.py
|   |       |   |   |   |   test_umath.py
|   |       |   |   |   |   test_umath_accuracy.py
|   |       |   |   |   |   test_umath_complex.py
|   |       |   |   |   |   test_unicode.py
|   |       |   |   |   |   test__exceptions.py
|   |       |   |   |   |   _locales.py
|   |       |   |   |   |   _natype.py
|   |       |   |   |   |   
|   |       |   |   |   +---data
|   |       |   |   |   |       astype_copy.pkl
|   |       |   |   |   |       generate_umath_validation_data.cpp
|   |       |   |   |   |       recarray_from_file.fits
|   |       |   |   |   |       umath-validation-set-arccos.csv
|   |       |   |   |   |       umath-validation-set-arccosh.csv
|   |       |   |   |   |       umath-validation-set-arcsin.csv
|   |       |   |   |   |       umath-validation-set-arcsinh.csv
|   |       |   |   |   |       umath-validation-set-arctan.csv
|   |       |   |   |   |       umath-validation-set-arctanh.csv
|   |       |   |   |   |       umath-validation-set-cbrt.csv
|   |       |   |   |   |       umath-validation-set-cos.csv
|   |       |   |   |   |       umath-validation-set-cosh.csv
|   |       |   |   |   |       umath-validation-set-exp.csv
|   |       |   |   |   |       umath-validation-set-exp2.csv
|   |       |   |   |   |       umath-validation-set-expm1.csv
|   |       |   |   |   |       umath-validation-set-log.csv
|   |       |   |   |   |       umath-validation-set-log10.csv
|   |       |   |   |   |       umath-validation-set-log1p.csv
|   |       |   |   |   |       umath-validation-set-log2.csv
|   |       |   |   |   |       umath-validation-set-README.txt
|   |       |   |   |   |       umath-validation-set-sin.csv
|   |       |   |   |   |       umath-validation-set-sinh.csv
|   |       |   |   |   |       umath-validation-set-tan.csv
|   |       |   |   |   |       umath-validation-set-tanh.csv
|   |       |   |   |   |       
|   |       |   |   |   \---examples
|   |       |   |   |       +---cython
|   |       |   |   |       |       checks.pyx
|   |       |   |   |       |       meson.build
|   |       |   |   |       |       setup.py
|   |       |   |   |       |       
|   |       |   |   |       \---limited_api
|   |       |   |   |               limited_api1.c
|   |       |   |   |               limited_api2.pyx
|   |       |   |   |               limited_api_latest.c
|   |       |   |   |               meson.build
|   |       |   |   |               setup.py
|   |       |   |   |               
|   |       |   |   \---__pycache__
|   |       |   |           arrayprint.cpython-312.pyc
|   |       |   |           einsumfunc.cpython-312.pyc
|   |       |   |           fromnumeric.cpython-312.pyc
|   |       |   |           function_base.cpython-312.pyc
|   |       |   |           getlimits.cpython-312.pyc
|   |       |   |           memmap.cpython-312.pyc
|   |       |   |           multiarray.cpython-312.pyc
|   |       |   |           numeric.cpython-312.pyc
|   |       |   |           numerictypes.cpython-312.pyc
|   |       |   |           overrides.cpython-312.pyc
|   |       |   |           printoptions.cpython-312.pyc
|   |       |   |           records.cpython-312.pyc
|   |       |   |           shape_base.cpython-312.pyc
|   |       |   |           umath.cpython-312.pyc
|   |       |   |           _add_newdocs.cpython-312.pyc
|   |       |   |           _add_newdocs_scalars.cpython-312.pyc
|   |       |   |           _asarray.cpython-312.pyc
|   |       |   |           _dtype.cpython-312.pyc
|   |       |   |           _dtype_ctypes.cpython-312.pyc
|   |       |   |           _exceptions.cpython-312.pyc
|   |       |   |           _internal.cpython-312.pyc
|   |       |   |           _machar.cpython-312.pyc
|   |       |   |           _methods.cpython-312.pyc
|   |       |   |           _string_helpers.cpython-312.pyc
|   |       |   |           _type_aliases.cpython-312.pyc
|   |       |   |           _ufunc_config.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---_pyinstaller
|   |       |   |   |   hook-numpy.py
|   |       |   |   |   hook-numpy.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---tests
|   |       |   |           pyinstaller-smoke.py
|   |       |   |           test_pyinstaller.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---_typing
|   |       |   |   |   _add_docstring.py
|   |       |   |   |   _array_like.py
|   |       |   |   |   _callable.pyi
|   |       |   |   |   _char_codes.py
|   |       |   |   |   _dtype_like.py
|   |       |   |   |   _extended_precision.py
|   |       |   |   |   _nbit.py
|   |       |   |   |   _nbit_base.py
|   |       |   |   |   _nbit_base.pyi
|   |       |   |   |   _nested_sequence.py
|   |       |   |   |   _scalars.py
|   |       |   |   |   _shape.py
|   |       |   |   |   _ufunc.py
|   |       |   |   |   _ufunc.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _array_like.cpython-312.pyc
|   |       |   |           _char_codes.cpython-312.pyc
|   |       |   |           _dtype_like.cpython-312.pyc
|   |       |   |           _nbit.cpython-312.pyc
|   |       |   |           _nbit_base.cpython-312.pyc
|   |       |   |           _nested_sequence.cpython-312.pyc
|   |       |   |           _scalars.cpython-312.pyc
|   |       |   |           _shape.cpython-312.pyc
|   |       |   |           _ufunc.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---_utils
|   |       |   |   |   _convertions.py
|   |       |   |   |   _convertions.pyi
|   |       |   |   |   _inspect.py
|   |       |   |   |   _inspect.pyi
|   |       |   |   |   _pep440.py
|   |       |   |   |   _pep440.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _convertions.cpython-312.pyc
|   |       |   |           _inspect.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           dtypes.cpython-312.pyc
|   |       |           exceptions.cpython-312.pyc
|   |       |           version.cpython-312.pyc
|   |       |           _array_api_info.cpython-312.pyc
|   |       |           _distributor_init.cpython-312.pyc
|   |       |           _expired_attrs_2_0.cpython-312.pyc
|   |       |           _globals.cpython-312.pyc
|   |       |           _pytesttester.cpython-312.pyc
|   |       |           __config__.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---numpy-2.3.3.dist-info
|   |       |       DELVEWHEEL
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       LICENSE.txt
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---numpy.libs
|   |       |       libscipy_openblas64_-860d95b1c38e637ce4509f5fa24fbf2a.dll
|   |       |       msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|   |       |       
|   |       +---packaging
|   |       |   |   markers.py
|   |       |   |   metadata.py
|   |       |   |   py.typed
|   |       |   |   requirements.py
|   |       |   |   specifiers.py
|   |       |   |   tags.py
|   |       |   |   utils.py
|   |       |   |   version.py
|   |       |   |   _elffile.py
|   |       |   |   _manylinux.py
|   |       |   |   _musllinux.py
|   |       |   |   _parser.py
|   |       |   |   _structures.py
|   |       |   |   _tokenizer.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---licenses
|   |       |   |       _spdx.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   \---__pycache__
|   |       |           version.cpython-312.pyc
|   |       |           _structures.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---packaging-25.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           LICENSE.APACHE
|   |       |           LICENSE.BSD
|   |       |           
|   |       +---pandas
|   |       |   |   conftest.py
|   |       |   |   pyproject.toml
|   |       |   |   testing.py
|   |       |   |   _typing.py
|   |       |   |   _version.py
|   |       |   |   _version_meson.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---api
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---extensions
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---indexers
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---interchange
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---types
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---typing
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---arrays
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---compat
|   |       |   |   |   compressors.py
|   |       |   |   |   pickle_compat.py
|   |       |   |   |   pyarrow.py
|   |       |   |   |   _constants.py
|   |       |   |   |   _optional.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---numpy
|   |       |   |   |   |   function.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           function.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           compressors.cpython-312.pyc
|   |       |   |           pickle_compat.cpython-312.pyc
|   |       |   |           pyarrow.cpython-312.pyc
|   |       |   |           _constants.cpython-312.pyc
|   |       |   |           _optional.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---core
|   |       |   |   |   accessor.py
|   |       |   |   |   algorithms.py
|   |       |   |   |   api.py
|   |       |   |   |   apply.py
|   |       |   |   |   arraylike.py
|   |       |   |   |   base.py
|   |       |   |   |   common.py
|   |       |   |   |   config_init.py
|   |       |   |   |   construction.py
|   |       |   |   |   flags.py
|   |       |   |   |   frame.py
|   |       |   |   |   generic.py
|   |       |   |   |   indexing.py
|   |       |   |   |   missing.py
|   |       |   |   |   nanops.py
|   |       |   |   |   resample.py
|   |       |   |   |   roperator.py
|   |       |   |   |   sample.py
|   |       |   |   |   series.py
|   |       |   |   |   shared_docs.py
|   |       |   |   |   sorting.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---arrays
|   |       |   |   |   |   base.py
|   |       |   |   |   |   boolean.py
|   |       |   |   |   |   categorical.py
|   |       |   |   |   |   datetimelike.py
|   |       |   |   |   |   datetimes.py
|   |       |   |   |   |   floating.py
|   |       |   |   |   |   integer.py
|   |       |   |   |   |   interval.py
|   |       |   |   |   |   masked.py
|   |       |   |   |   |   numeric.py
|   |       |   |   |   |   numpy_.py
|   |       |   |   |   |   period.py
|   |       |   |   |   |   string_.py
|   |       |   |   |   |   string_arrow.py
|   |       |   |   |   |   timedeltas.py
|   |       |   |   |   |   _arrow_string_mixins.py
|   |       |   |   |   |   _mixins.py
|   |       |   |   |   |   _ranges.py
|   |       |   |   |   |   _utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---arrow
|   |       |   |   |   |   |   accessors.py
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   extension_types.py
|   |       |   |   |   |   |   _arrow_utils.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           accessors.cpython-312.pyc
|   |       |   |   |   |           array.cpython-312.pyc
|   |       |   |   |   |           __init__.cpython-312.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---sparse
|   |       |   |   |   |   |   accessor.py
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   scipy_sparse.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           accessor.cpython-312.pyc
|   |       |   |   |   |           array.cpython-312.pyc
|   |       |   |   |   |           __init__.cpython-312.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-312.pyc
|   |       |   |   |           boolean.cpython-312.pyc
|   |       |   |   |           categorical.cpython-312.pyc
|   |       |   |   |           datetimelike.cpython-312.pyc
|   |       |   |   |           datetimes.cpython-312.pyc
|   |       |   |   |           floating.cpython-312.pyc
|   |       |   |   |           integer.cpython-312.pyc
|   |       |   |   |           interval.cpython-312.pyc
|   |       |   |   |           masked.cpython-312.pyc
|   |       |   |   |           numeric.cpython-312.pyc
|   |       |   |   |           numpy_.cpython-312.pyc
|   |       |   |   |           period.cpython-312.pyc
|   |       |   |   |           string_.cpython-312.pyc
|   |       |   |   |           string_arrow.cpython-312.pyc
|   |       |   |   |           timedeltas.cpython-312.pyc
|   |       |   |   |           _arrow_string_mixins.cpython-312.pyc
|   |       |   |   |           _mixins.cpython-312.pyc
|   |       |   |   |           _ranges.cpython-312.pyc
|   |       |   |   |           _utils.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---array_algos
|   |       |   |   |   |   datetimelike_accumulations.py
|   |       |   |   |   |   masked_accumulations.py
|   |       |   |   |   |   masked_reductions.py
|   |       |   |   |   |   putmask.py
|   |       |   |   |   |   quantile.py
|   |       |   |   |   |   replace.py
|   |       |   |   |   |   take.py
|   |       |   |   |   |   transforms.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           datetimelike_accumulations.cpython-312.pyc
|   |       |   |   |           masked_accumulations.cpython-312.pyc
|   |       |   |   |           masked_reductions.cpython-312.pyc
|   |       |   |   |           putmask.cpython-312.pyc
|   |       |   |   |           quantile.cpython-312.pyc
|   |       |   |   |           replace.cpython-312.pyc
|   |       |   |   |           take.cpython-312.pyc
|   |       |   |   |           transforms.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---computation
|   |       |   |   |   |   align.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   check.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   engines.py
|   |       |   |   |   |   eval.py
|   |       |   |   |   |   expr.py
|   |       |   |   |   |   expressions.py
|   |       |   |   |   |   ops.py
|   |       |   |   |   |   parsing.py
|   |       |   |   |   |   pytables.py
|   |       |   |   |   |   scope.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           align.cpython-312.pyc
|   |       |   |   |           api.cpython-312.pyc
|   |       |   |   |           check.cpython-312.pyc
|   |       |   |   |           common.cpython-312.pyc
|   |       |   |   |           engines.cpython-312.pyc
|   |       |   |   |           eval.cpython-312.pyc
|   |       |   |   |           expr.cpython-312.pyc
|   |       |   |   |           expressions.cpython-312.pyc
|   |       |   |   |           ops.cpython-312.pyc
|   |       |   |   |           parsing.cpython-312.pyc
|   |       |   |   |           pytables.cpython-312.pyc
|   |       |   |   |           scope.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---dtypes
|   |       |   |   |   |   api.py
|   |       |   |   |   |   astype.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   cast.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   concat.py
|   |       |   |   |   |   dtypes.py
|   |       |   |   |   |   generic.py
|   |       |   |   |   |   inference.py
|   |       |   |   |   |   missing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-312.pyc
|   |       |   |   |           astype.cpython-312.pyc
|   |       |   |   |           base.cpython-312.pyc
|   |       |   |   |           cast.cpython-312.pyc
|   |       |   |   |           common.cpython-312.pyc
|   |       |   |   |           concat.cpython-312.pyc
|   |       |   |   |           dtypes.cpython-312.pyc
|   |       |   |   |           generic.cpython-312.pyc
|   |       |   |   |           inference.cpython-312.pyc
|   |       |   |   |           missing.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---groupby
|   |       |   |   |   |   base.py
|   |       |   |   |   |   categorical.py
|   |       |   |   |   |   generic.py
|   |       |   |   |   |   groupby.py
|   |       |   |   |   |   grouper.py
|   |       |   |   |   |   indexing.py
|   |       |   |   |   |   numba_.py
|   |       |   |   |   |   ops.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-312.pyc
|   |       |   |   |           categorical.cpython-312.pyc
|   |       |   |   |           generic.cpython-312.pyc
|   |       |   |   |           groupby.cpython-312.pyc
|   |       |   |   |           grouper.cpython-312.pyc
|   |       |   |   |           indexing.cpython-312.pyc
|   |       |   |   |           numba_.cpython-312.pyc
|   |       |   |   |           ops.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---indexers
|   |       |   |   |   |   objects.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           objects.cpython-312.pyc
|   |       |   |   |           utils.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---indexes
|   |       |   |   |   |   accessors.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   category.py
|   |       |   |   |   |   datetimelike.py
|   |       |   |   |   |   datetimes.py
|   |       |   |   |   |   extension.py
|   |       |   |   |   |   frozen.py
|   |       |   |   |   |   interval.py
|   |       |   |   |   |   multi.py
|   |       |   |   |   |   period.py
|   |       |   |   |   |   range.py
|   |       |   |   |   |   timedeltas.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           accessors.cpython-312.pyc
|   |       |   |   |           api.cpython-312.pyc
|   |       |   |   |           base.cpython-312.pyc
|   |       |   |   |           category.cpython-312.pyc
|   |       |   |   |           datetimelike.cpython-312.pyc
|   |       |   |   |           datetimes.cpython-312.pyc
|   |       |   |   |           extension.cpython-312.pyc
|   |       |   |   |           frozen.cpython-312.pyc
|   |       |   |   |           interval.cpython-312.pyc
|   |       |   |   |           multi.cpython-312.pyc
|   |       |   |   |           period.cpython-312.pyc
|   |       |   |   |           range.cpython-312.pyc
|   |       |   |   |           timedeltas.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---interchange
|   |       |   |   |   |   buffer.py
|   |       |   |   |   |   column.py
|   |       |   |   |   |   dataframe.py
|   |       |   |   |   |   dataframe_protocol.py
|   |       |   |   |   |   from_dataframe.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           dataframe_protocol.cpython-312.pyc
|   |       |   |   |           from_dataframe.cpython-312.pyc
|   |       |   |   |           utils.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---internals
|   |       |   |   |   |   api.py
|   |       |   |   |   |   array_manager.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   blocks.py
|   |       |   |   |   |   concat.py
|   |       |   |   |   |   construction.py
|   |       |   |   |   |   managers.py
|   |       |   |   |   |   ops.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-312.pyc
|   |       |   |   |           array_manager.cpython-312.pyc
|   |       |   |   |           base.cpython-312.pyc
|   |       |   |   |           blocks.cpython-312.pyc
|   |       |   |   |           concat.cpython-312.pyc
|   |       |   |   |           construction.cpython-312.pyc
|   |       |   |   |           managers.cpython-312.pyc
|   |       |   |   |           ops.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---methods
|   |       |   |   |   |   describe.py
|   |       |   |   |   |   selectn.py
|   |       |   |   |   |   to_dict.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           describe.cpython-312.pyc
|   |       |   |   |           selectn.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---ops
|   |       |   |   |   |   array_ops.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   dispatch.py
|   |       |   |   |   |   docstrings.py
|   |       |   |   |   |   invalid.py
|   |       |   |   |   |   mask_ops.py
|   |       |   |   |   |   missing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           array_ops.cpython-312.pyc
|   |       |   |   |           common.cpython-312.pyc
|   |       |   |   |           dispatch.cpython-312.pyc
|   |       |   |   |           docstrings.cpython-312.pyc
|   |       |   |   |           invalid.cpython-312.pyc
|   |       |   |   |           mask_ops.cpython-312.pyc
|   |       |   |   |           missing.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---reshape
|   |       |   |   |   |   api.py
|   |       |   |   |   |   concat.py
|   |       |   |   |   |   encoding.py
|   |       |   |   |   |   melt.py
|   |       |   |   |   |   merge.py
|   |       |   |   |   |   pivot.py
|   |       |   |   |   |   reshape.py
|   |       |   |   |   |   tile.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-312.pyc
|   |       |   |   |           concat.cpython-312.pyc
|   |       |   |   |           encoding.cpython-312.pyc
|   |       |   |   |           melt.cpython-312.pyc
|   |       |   |   |           merge.cpython-312.pyc
|   |       |   |   |           pivot.cpython-312.pyc
|   |       |   |   |           tile.cpython-312.pyc
|   |       |   |   |           util.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---sparse
|   |       |   |   |       api.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---strings
|   |       |   |   |   |   accessor.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   object_array.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           accessor.cpython-312.pyc
|   |       |   |   |           base.cpython-312.pyc
|   |       |   |   |           object_array.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---tools
|   |       |   |   |   |   datetimes.py
|   |       |   |   |   |   numeric.py
|   |       |   |   |   |   timedeltas.py
|   |       |   |   |   |   times.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           datetimes.cpython-312.pyc
|   |       |   |   |           numeric.cpython-312.pyc
|   |       |   |   |           timedeltas.cpython-312.pyc
|   |       |   |   |           times.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---util
|   |       |   |   |   |   hashing.py
|   |       |   |   |   |   numba_.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           hashing.cpython-312.pyc
|   |       |   |   |           numba_.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---window
|   |       |   |   |   |   common.py
|   |       |   |   |   |   doc.py
|   |       |   |   |   |   ewm.py
|   |       |   |   |   |   expanding.py
|   |       |   |   |   |   numba_.py
|   |       |   |   |   |   online.py
|   |       |   |   |   |   rolling.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-312.pyc
|   |       |   |   |           doc.cpython-312.pyc
|   |       |   |   |           ewm.cpython-312.pyc
|   |       |   |   |           expanding.cpython-312.pyc
|   |       |   |   |           numba_.cpython-312.pyc
|   |       |   |   |           online.cpython-312.pyc
|   |       |   |   |           rolling.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---_numba
|   |       |   |   |   |   executor.py
|   |       |   |   |   |   extensions.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---kernels
|   |       |   |   |   |       mean_.py
|   |       |   |   |   |       min_max_.py
|   |       |   |   |   |       shared.py
|   |       |   |   |   |       sum_.py
|   |       |   |   |   |       var_.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---__pycache__
|   |       |   |   |           executor.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           accessor.cpython-312.pyc
|   |       |   |           algorithms.cpython-312.pyc
|   |       |   |           api.cpython-312.pyc
|   |       |   |           apply.cpython-312.pyc
|   |       |   |           arraylike.cpython-312.pyc
|   |       |   |           base.cpython-312.pyc
|   |       |   |           common.cpython-312.pyc
|   |       |   |           config_init.cpython-312.pyc
|   |       |   |           construction.cpython-312.pyc
|   |       |   |           flags.cpython-312.pyc
|   |       |   |           frame.cpython-312.pyc
|   |       |   |           generic.cpython-312.pyc
|   |       |   |           indexing.cpython-312.pyc
|   |       |   |           missing.cpython-312.pyc
|   |       |   |           nanops.cpython-312.pyc
|   |       |   |           resample.cpython-312.pyc
|   |       |   |           roperator.cpython-312.pyc
|   |       |   |           sample.cpython-312.pyc
|   |       |   |           series.cpython-312.pyc
|   |       |   |           shared_docs.cpython-312.pyc
|   |       |   |           sorting.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---errors
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---io
|   |       |   |   |   api.py
|   |       |   |   |   clipboards.py
|   |       |   |   |   common.py
|   |       |   |   |   feather_format.py
|   |       |   |   |   gbq.py
|   |       |   |   |   html.py
|   |       |   |   |   orc.py
|   |       |   |   |   parquet.py
|   |       |   |   |   pickle.py
|   |       |   |   |   pytables.py
|   |       |   |   |   spss.py
|   |       |   |   |   sql.py
|   |       |   |   |   stata.py
|   |       |   |   |   xml.py
|   |       |   |   |   _util.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---clipboard
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---excel
|   |       |   |   |   |   _base.py
|   |       |   |   |   |   _calamine.py
|   |       |   |   |   |   _odfreader.py
|   |       |   |   |   |   _odswriter.py
|   |       |   |   |   |   _openpyxl.py
|   |       |   |   |   |   _pyxlsb.py
|   |       |   |   |   |   _util.py
|   |       |   |   |   |   _xlrd.py
|   |       |   |   |   |   _xlsxwriter.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _base.cpython-312.pyc
|   |       |   |   |           _calamine.cpython-312.pyc
|   |       |   |   |           _odfreader.cpython-312.pyc
|   |       |   |   |           _odswriter.cpython-312.pyc
|   |       |   |   |           _openpyxl.cpython-312.pyc
|   |       |   |   |           _pyxlsb.cpython-312.pyc
|   |       |   |   |           _util.cpython-312.pyc
|   |       |   |   |           _xlrd.cpython-312.pyc
|   |       |   |   |           _xlsxwriter.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---formats
|   |       |   |   |   |   console.py
|   |       |   |   |   |   css.py
|   |       |   |   |   |   csvs.py
|   |       |   |   |   |   excel.py
|   |       |   |   |   |   format.py
|   |       |   |   |   |   html.py
|   |       |   |   |   |   info.py
|   |       |   |   |   |   printing.py
|   |       |   |   |   |   string.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   style_render.py
|   |       |   |   |   |   xml.py
|   |       |   |   |   |   _color_data.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---templates
|   |       |   |   |   |       html.tpl
|   |       |   |   |   |       html_style.tpl
|   |       |   |   |   |       html_table.tpl
|   |       |   |   |   |       latex.tpl
|   |       |   |   |   |       latex_longtable.tpl
|   |       |   |   |   |       latex_table.tpl
|   |       |   |   |   |       string.tpl
|   |       |   |   |   |       
|   |       |   |   |   \---__pycache__
|   |       |   |   |           console.cpython-312.pyc
|   |       |   |   |           format.cpython-312.pyc
|   |       |   |   |           info.cpython-312.pyc
|   |       |   |   |           printing.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---json
|   |       |   |   |   |   _json.py
|   |       |   |   |   |   _normalize.py
|   |       |   |   |   |   _table_schema.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _json.cpython-312.pyc
|   |       |   |   |           _normalize.cpython-312.pyc
|   |       |   |   |           _table_schema.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---parsers
|   |       |   |   |   |   arrow_parser_wrapper.py
|   |       |   |   |   |   base_parser.py
|   |       |   |   |   |   c_parser_wrapper.py
|   |       |   |   |   |   python_parser.py
|   |       |   |   |   |   readers.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           arrow_parser_wrapper.cpython-312.pyc
|   |       |   |   |           base_parser.cpython-312.pyc
|   |       |   |   |           c_parser_wrapper.cpython-312.pyc
|   |       |   |   |           python_parser.cpython-312.pyc
|   |       |   |   |           readers.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---sas
|   |       |   |   |   |   sas7bdat.py
|   |       |   |   |   |   sasreader.py
|   |       |   |   |   |   sas_constants.py
|   |       |   |   |   |   sas_xport.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           sasreader.cpython-312.pyc
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           api.cpython-312.pyc
|   |       |   |           clipboards.cpython-312.pyc
|   |       |   |           common.cpython-312.pyc
|   |       |   |           feather_format.cpython-312.pyc
|   |       |   |           gbq.cpython-312.pyc
|   |       |   |           html.cpython-312.pyc
|   |       |   |           orc.cpython-312.pyc
|   |       |   |           parquet.cpython-312.pyc
|   |       |   |           pickle.cpython-312.pyc
|   |       |   |           pytables.cpython-312.pyc
|   |       |   |           spss.cpython-312.pyc
|   |       |   |           sql.cpython-312.pyc
|   |       |   |           stata.cpython-312.pyc
|   |       |   |           xml.cpython-312.pyc
|   |       |   |           _util.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---plotting
|   |       |   |   |   _core.py
|   |       |   |   |   _misc.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---_matplotlib
|   |       |   |   |       boxplot.py
|   |       |   |   |       converter.py
|   |       |   |   |       core.py
|   |       |   |   |       groupby.py
|   |       |   |   |       hist.py
|   |       |   |   |       misc.py
|   |       |   |   |       style.py
|   |       |   |   |       timeseries.py
|   |       |   |   |       tools.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---__pycache__
|   |       |   |           _core.cpython-312.pyc
|   |       |   |           _misc.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---tests
|   |       |   |   |   test_aggregation.py
|   |       |   |   |   test_algos.py
|   |       |   |   |   test_common.py
|   |       |   |   |   test_downstream.py
|   |       |   |   |   test_errors.py
|   |       |   |   |   test_expressions.py
|   |       |   |   |   test_flags.py
|   |       |   |   |   test_multilevel.py
|   |       |   |   |   test_nanops.py
|   |       |   |   |   test_optional_dependency.py
|   |       |   |   |   test_register_accessor.py
|   |       |   |   |   test_sorting.py
|   |       |   |   |   test_take.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---api
|   |       |   |   |       test_api.py
|   |       |   |   |       test_types.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---apply
|   |       |   |   |       common.py
|   |       |   |   |       test_frame_apply.py
|   |       |   |   |       test_frame_apply_relabeling.py
|   |       |   |   |       test_frame_transform.py
|   |       |   |   |       test_invalid_arg.py
|   |       |   |   |       test_numba.py
|   |       |   |   |       test_series_apply.py
|   |       |   |   |       test_series_apply_relabeling.py
|   |       |   |   |       test_series_transform.py
|   |       |   |   |       test_str.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---arithmetic
|   |       |   |   |       common.py
|   |       |   |   |       conftest.py
|   |       |   |   |       test_array_ops.py
|   |       |   |   |       test_categorical.py
|   |       |   |   |       test_datetime64.py
|   |       |   |   |       test_interval.py
|   |       |   |   |       test_numeric.py
|   |       |   |   |       test_object.py
|   |       |   |   |       test_period.py
|   |       |   |   |       test_timedelta64.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---arrays
|   |       |   |   |   |   masked_shared.py
|   |       |   |   |   |   test_array.py
|   |       |   |   |   |   test_datetimelike.py
|   |       |   |   |   |   test_datetimes.py
|   |       |   |   |   |   test_ndarray_backed.py
|   |       |   |   |   |   test_period.py
|   |       |   |   |   |   test_timedeltas.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---boolean
|   |       |   |   |   |       test_arithmetic.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_comparison.py
|   |       |   |   |   |       test_construction.py
|   |       |   |   |   |       test_function.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_logical.py
|   |       |   |   |   |       test_ops.py
|   |       |   |   |   |       test_reduction.py
|   |       |   |   |   |       test_repr.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---categorical
|   |       |   |   |   |       test_algos.py
|   |       |   |   |   |       test_analytics.py
|   |       |   |   |   |       test_api.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_dtypes.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_map.py
|   |       |   |   |   |       test_missing.py
|   |       |   |   |   |       test_operators.py
|   |       |   |   |   |       test_replace.py
|   |       |   |   |   |       test_repr.py
|   |       |   |   |   |       test_sorting.py
|   |       |   |   |   |       test_subclass.py
|   |       |   |   |   |       test_take.py
|   |       |   |   |   |       test_warnings.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---datetimes
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_cumulative.py
|   |       |   |   |   |       test_reductions.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---floating
|   |       |   |   |   |       conftest.py
|   |       |   |   |   |       test_arithmetic.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_comparison.py
|   |       |   |   |   |       test_concat.py
|   |       |   |   |   |       test_construction.py
|   |       |   |   |   |       test_contains.py
|   |       |   |   |   |       test_function.py
|   |       |   |   |   |       test_repr.py
|   |       |   |   |   |       test_to_numpy.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---integer
|   |       |   |   |   |       conftest.py
|   |       |   |   |   |       test_arithmetic.py
|   |       |   |   |   |       test_comparison.py
|   |       |   |   |   |       test_concat.py
|   |       |   |   |   |       test_construction.py
|   |       |   |   |   |       test_dtypes.py
|   |       |   |   |   |       test_function.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_reduction.py
|   |       |   |   |   |       test_repr.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---interval
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_formats.py
|   |       |   |   |   |       test_interval.py
|   |       |   |   |   |       test_interval_pyarrow.py
|   |       |   |   |   |       test_overlaps.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---masked
|   |       |   |   |   |       test_arithmetic.py
|   |       |   |   |   |       test_arrow_compat.py
|   |       |   |   |   |       test_function.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---numpy_
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_numpy.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---period
|   |       |   |   |   |       test_arrow_compat.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_reductions.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---sparse
|   |       |   |   |   |       test_accessor.py
|   |       |   |   |   |       test_arithmetics.py
|   |       |   |   |   |       test_array.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_combine_concat.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_dtype.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_libsparse.py
|   |       |   |   |   |       test_reductions.py
|   |       |   |   |   |       test_unary.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---string_
|   |       |   |   |   |       test_concat.py
|   |       |   |   |   |       test_string.py
|   |       |   |   |   |       test_string_arrow.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---timedeltas
|   |       |   |   |           test_constructors.py
|   |       |   |   |           test_cumulative.py
|   |       |   |   |           test_reductions.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---base
|   |       |   |   |       common.py
|   |       |   |   |       test_constructors.py
|   |       |   |   |       test_conversion.py
|   |       |   |   |       test_fillna.py
|   |       |   |   |       test_misc.py
|   |       |   |   |       test_transpose.py
|   |       |   |   |       test_unique.py
|   |       |   |   |       test_value_counts.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---computation
|   |       |   |   |       test_compat.py
|   |       |   |   |       test_eval.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---config
|   |       |   |   |       test_config.py
|   |       |   |   |       test_localization.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---construction
|   |       |   |   |       test_extract_array.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---copy_view
|   |       |   |   |   |   test_array.py
|   |       |   |   |   |   test_astype.py
|   |       |   |   |   |   test_chained_assignment_deprecation.py
|   |       |   |   |   |   test_clip.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_core_functionalities.py
|   |       |   |   |   |   test_functions.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_internals.py
|   |       |   |   |   |   test_interp_fillna.py
|   |       |   |   |   |   test_methods.py
|   |       |   |   |   |   test_replace.py
|   |       |   |   |   |   test_setitem.py
|   |       |   |   |   |   test_util.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---index
|   |       |   |   |           test_datetimeindex.py
|   |       |   |   |           test_index.py
|   |       |   |   |           test_periodindex.py
|   |       |   |   |           test_timedeltaindex.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---dtypes
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_concat.py
|   |       |   |   |   |   test_dtypes.py
|   |       |   |   |   |   test_generic.py
|   |       |   |   |   |   test_inference.py
|   |       |   |   |   |   test_missing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---cast
|   |       |   |   |           test_can_hold_element.py
|   |       |   |   |           test_construct_from_scalar.py
|   |       |   |   |           test_construct_ndarray.py
|   |       |   |   |           test_construct_object_arr.py
|   |       |   |   |           test_dict_compat.py
|   |       |   |   |           test_downcast.py
|   |       |   |   |           test_find_common_type.py
|   |       |   |   |           test_infer_datetimelike.py
|   |       |   |   |           test_infer_dtype.py
|   |       |   |   |           test_maybe_box_native.py
|   |       |   |   |           test_promote.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---extension
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_arrow.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_datetime.py
|   |       |   |   |   |   test_extension.py
|   |       |   |   |   |   test_interval.py
|   |       |   |   |   |   test_masked.py
|   |       |   |   |   |   test_numpy.py
|   |       |   |   |   |   test_period.py
|   |       |   |   |   |   test_sparse.py
|   |       |   |   |   |   test_string.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---array_with_attr
|   |       |   |   |   |       array.py
|   |       |   |   |   |       test_array_with_attr.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---base
|   |       |   |   |   |       accumulate.py
|   |       |   |   |   |       base.py
|   |       |   |   |   |       casting.py
|   |       |   |   |   |       constructors.py
|   |       |   |   |   |       dim2.py
|   |       |   |   |   |       dtype.py
|   |       |   |   |   |       getitem.py
|   |       |   |   |   |       groupby.py
|   |       |   |   |   |       index.py
|   |       |   |   |   |       interface.py
|   |       |   |   |   |       io.py
|   |       |   |   |   |       methods.py
|   |       |   |   |   |       missing.py
|   |       |   |   |   |       ops.py
|   |       |   |   |   |       printing.py
|   |       |   |   |   |       reduce.py
|   |       |   |   |   |       reshaping.py
|   |       |   |   |   |       setitem.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---date
|   |       |   |   |   |       array.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---decimal
|   |       |   |   |   |       array.py
|   |       |   |   |   |       test_decimal.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---json
|   |       |   |   |   |       array.py
|   |       |   |   |   |       test_json.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---list
|   |       |   |   |           array.py
|   |       |   |   |           test_list.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---frame
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_alter_axes.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   test_arrow_interface.py
|   |       |   |   |   |   test_block_internals.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_cumulative.py
|   |       |   |   |   |   test_iteration.py
|   |       |   |   |   |   test_logical_ops.py
|   |       |   |   |   |   test_nonunique_indexes.py
|   |       |   |   |   |   test_npfuncs.py
|   |       |   |   |   |   test_query_eval.py
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_repr.py
|   |       |   |   |   |   test_stack_unstack.py
|   |       |   |   |   |   test_subclass.py
|   |       |   |   |   |   test_ufunc.py
|   |       |   |   |   |   test_unary.py
|   |       |   |   |   |   test_validate.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---constructors
|   |       |   |   |   |       test_from_dict.py
|   |       |   |   |   |       test_from_records.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---indexing
|   |       |   |   |   |       test_coercion.py
|   |       |   |   |   |       test_delitem.py
|   |       |   |   |   |       test_get.py
|   |       |   |   |   |       test_getitem.py
|   |       |   |   |   |       test_get_value.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_insert.py
|   |       |   |   |   |       test_mask.py
|   |       |   |   |   |       test_setitem.py
|   |       |   |   |   |       test_set_value.py
|   |       |   |   |   |       test_take.py
|   |       |   |   |   |       test_where.py
|   |       |   |   |   |       test_xs.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---methods
|   |       |   |   |           test_add_prefix_suffix.py
|   |       |   |   |           test_align.py
|   |       |   |   |           test_asfreq.py
|   |       |   |   |           test_asof.py
|   |       |   |   |           test_assign.py
|   |       |   |   |           test_astype.py
|   |       |   |   |           test_at_time.py
|   |       |   |   |           test_between_time.py
|   |       |   |   |           test_clip.py
|   |       |   |   |           test_combine.py
|   |       |   |   |           test_combine_first.py
|   |       |   |   |           test_compare.py
|   |       |   |   |           test_convert_dtypes.py
|   |       |   |   |           test_copy.py
|   |       |   |   |           test_count.py
|   |       |   |   |           test_cov_corr.py
|   |       |   |   |           test_describe.py
|   |       |   |   |           test_diff.py
|   |       |   |   |           test_dot.py
|   |       |   |   |           test_drop.py
|   |       |   |   |           test_droplevel.py
|   |       |   |   |           test_dropna.py
|   |       |   |   |           test_drop_duplicates.py
|   |       |   |   |           test_dtypes.py
|   |       |   |   |           test_duplicated.py
|   |       |   |   |           test_equals.py
|   |       |   |   |           test_explode.py
|   |       |   |   |           test_fillna.py
|   |       |   |   |           test_filter.py
|   |       |   |   |           test_first_and_last.py
|   |       |   |   |           test_first_valid_index.py
|   |       |   |   |           test_get_numeric_data.py
|   |       |   |   |           test_head_tail.py
|   |       |   |   |           test_infer_objects.py
|   |       |   |   |           test_info.py
|   |       |   |   |           test_interpolate.py
|   |       |   |   |           test_isetitem.py
|   |       |   |   |           test_isin.py
|   |       |   |   |           test_is_homogeneous_dtype.py
|   |       |   |   |           test_iterrows.py
|   |       |   |   |           test_join.py
|   |       |   |   |           test_map.py
|   |       |   |   |           test_matmul.py
|   |       |   |   |           test_nlargest.py
|   |       |   |   |           test_pct_change.py
|   |       |   |   |           test_pipe.py
|   |       |   |   |           test_pop.py
|   |       |   |   |           test_quantile.py
|   |       |   |   |           test_rank.py
|   |       |   |   |           test_reindex.py
|   |       |   |   |           test_reindex_like.py
|   |       |   |   |           test_rename.py
|   |       |   |   |           test_rename_axis.py
|   |       |   |   |           test_reorder_levels.py
|   |       |   |   |           test_replace.py
|   |       |   |   |           test_reset_index.py
|   |       |   |   |           test_round.py
|   |       |   |   |           test_sample.py
|   |       |   |   |           test_select_dtypes.py
|   |       |   |   |           test_set_axis.py
|   |       |   |   |           test_set_index.py
|   |       |   |   |           test_shift.py
|   |       |   |   |           test_size.py
|   |       |   |   |           test_sort_index.py
|   |       |   |   |           test_sort_values.py
|   |       |   |   |           test_swapaxes.py
|   |       |   |   |           test_swaplevel.py
|   |       |   |   |           test_to_csv.py
|   |       |   |   |           test_to_dict.py
|   |       |   |   |           test_to_dict_of_blocks.py
|   |       |   |   |           test_to_numpy.py
|   |       |   |   |           test_to_period.py
|   |       |   |   |           test_to_records.py
|   |       |   |   |           test_to_timestamp.py
|   |       |   |   |           test_transpose.py
|   |       |   |   |           test_truncate.py
|   |       |   |   |           test_tz_convert.py
|   |       |   |   |           test_tz_localize.py
|   |       |   |   |           test_update.py
|   |       |   |   |           test_values.py
|   |       |   |   |           test_value_counts.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---generic
|   |       |   |   |       test_duplicate_labels.py
|   |       |   |   |       test_finalize.py
|   |       |   |   |       test_frame.py
|   |       |   |   |       test_generic.py
|   |       |   |   |       test_label_or_level_utils.py
|   |       |   |   |       test_series.py
|   |       |   |   |       test_to_xarray.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---groupby
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_all_methods.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_apply.py
|   |       |   |   |   |   test_apply_mutate.py
|   |       |   |   |   |   test_bin_groupby.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_counting.py
|   |       |   |   |   |   test_cumulative.py
|   |       |   |   |   |   test_filters.py
|   |       |   |   |   |   test_groupby.py
|   |       |   |   |   |   test_groupby_dropna.py
|   |       |   |   |   |   test_groupby_subclass.py
|   |       |   |   |   |   test_grouping.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_index_as_string.py
|   |       |   |   |   |   test_libgroupby.py
|   |       |   |   |   |   test_missing.py
|   |       |   |   |   |   test_numba.py
|   |       |   |   |   |   test_numeric_only.py
|   |       |   |   |   |   test_pipe.py
|   |       |   |   |   |   test_raises.py
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_timegrouper.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---aggregate
|   |       |   |   |   |       test_aggregate.py
|   |       |   |   |   |       test_cython.py
|   |       |   |   |   |       test_numba.py
|   |       |   |   |   |       test_other.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---methods
|   |       |   |   |   |       test_corrwith.py
|   |       |   |   |   |       test_describe.py
|   |       |   |   |   |       test_groupby_shift_diff.py
|   |       |   |   |   |       test_is_monotonic.py
|   |       |   |   |   |       test_nlargest_nsmallest.py
|   |       |   |   |   |       test_nth.py
|   |       |   |   |   |       test_quantile.py
|   |       |   |   |   |       test_rank.py
|   |       |   |   |   |       test_sample.py
|   |       |   |   |   |       test_size.py
|   |       |   |   |   |       test_skew.py
|   |       |   |   |   |       test_value_counts.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---transform
|   |       |   |   |           test_numba.py
|   |       |   |   |           test_transform.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---indexes
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_any_index.py
|   |       |   |   |   |   test_base.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_datetimelike.py
|   |       |   |   |   |   test_engines.py
|   |       |   |   |   |   test_frozen.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_index_new.py
|   |       |   |   |   |   test_numpy_compat.py
|   |       |   |   |   |   test_old_base.py
|   |       |   |   |   |   test_setops.py
|   |       |   |   |   |   test_subclass.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---base_class
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_formats.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_pickle.py
|   |       |   |   |   |       test_reshape.py
|   |       |   |   |   |       test_setops.py
|   |       |   |   |   |       test_where.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---categorical
|   |       |   |   |   |       test_append.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_category.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_equals.py
|   |       |   |   |   |       test_fillna.py
|   |       |   |   |   |       test_formats.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_map.py
|   |       |   |   |   |       test_reindex.py
|   |       |   |   |   |       test_setops.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---datetimelike_
|   |       |   |   |   |       test_drop_duplicates.py
|   |       |   |   |   |       test_equals.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_is_monotonic.py
|   |       |   |   |   |       test_nat.py
|   |       |   |   |   |       test_sort_values.py
|   |       |   |   |   |       test_value_counts.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---datetimes
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_datetime.py
|   |       |   |   |   |   |   test_date_range.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_freq_attr.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_iter.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_npfuncs.py
|   |       |   |   |   |   |   test_ops.py
|   |       |   |   |   |   |   test_partial_slicing.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_reindex.py
|   |       |   |   |   |   |   test_scalar_compat.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_timezones.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---methods
|   |       |   |   |   |           test_asof.py
|   |       |   |   |   |           test_astype.py
|   |       |   |   |   |           test_delete.py
|   |       |   |   |   |           test_factorize.py
|   |       |   |   |   |           test_fillna.py
|   |       |   |   |   |           test_insert.py
|   |       |   |   |   |           test_isocalendar.py
|   |       |   |   |   |           test_map.py
|   |       |   |   |   |           test_normalize.py
|   |       |   |   |   |           test_repeat.py
|   |       |   |   |   |           test_resolution.py
|   |       |   |   |   |           test_round.py
|   |       |   |   |   |           test_shift.py
|   |       |   |   |   |           test_snap.py
|   |       |   |   |   |           test_to_frame.py
|   |       |   |   |   |           test_to_julian_date.py
|   |       |   |   |   |           test_to_period.py
|   |       |   |   |   |           test_to_pydatetime.py
|   |       |   |   |   |           test_to_series.py
|   |       |   |   |   |           test_tz_convert.py
|   |       |   |   |   |           test_tz_localize.py
|   |       |   |   |   |           test_unique.py
|   |       |   |   |   |           __init__.py
|   |       |   |   |   |           
|   |       |   |   |   +---interval
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_equals.py
|   |       |   |   |   |       test_formats.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_interval.py
|   |       |   |   |   |       test_interval_range.py
|   |       |   |   |   |       test_interval_tree.py
|   |       |   |   |   |       test_join.py
|   |       |   |   |   |       test_pickle.py
|   |       |   |   |   |       test_setops.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---multi
|   |       |   |   |   |       conftest.py
|   |       |   |   |   |       test_analytics.py
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_compat.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_conversion.py
|   |       |   |   |   |       test_copy.py
|   |       |   |   |   |       test_drop.py
|   |       |   |   |   |       test_duplicates.py
|   |       |   |   |   |       test_equivalence.py
|   |       |   |   |   |       test_formats.py
|   |       |   |   |   |       test_get_level_values.py
|   |       |   |   |   |       test_get_set.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_integrity.py
|   |       |   |   |   |       test_isin.py
|   |       |   |   |   |       test_join.py
|   |       |   |   |   |       test_lexsort.py
|   |       |   |   |   |       test_missing.py
|   |       |   |   |   |       test_monotonic.py
|   |       |   |   |   |       test_names.py
|   |       |   |   |   |       test_partial_indexing.py
|   |       |   |   |   |       test_pickle.py
|   |       |   |   |   |       test_reindex.py
|   |       |   |   |   |       test_reshape.py
|   |       |   |   |   |       test_setops.py
|   |       |   |   |   |       test_sorting.py
|   |       |   |   |   |       test_take.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---numeric
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_join.py
|   |       |   |   |   |       test_numeric.py
|   |       |   |   |   |       test_setops.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---object
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---period
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_freq_attr.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_monotonic.py
|   |       |   |   |   |   |   test_partial_slicing.py
|   |       |   |   |   |   |   test_period.py
|   |       |   |   |   |   |   test_period_range.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_resolution.py
|   |       |   |   |   |   |   test_scalar_compat.py
|   |       |   |   |   |   |   test_searchsorted.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_tools.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---methods
|   |       |   |   |   |           test_asfreq.py
|   |       |   |   |   |           test_astype.py
|   |       |   |   |   |           test_factorize.py
|   |       |   |   |   |           test_fillna.py
|   |       |   |   |   |           test_insert.py
|   |       |   |   |   |           test_is_full.py
|   |       |   |   |   |           test_repeat.py
|   |       |   |   |   |           test_shift.py
|   |       |   |   |   |           test_to_timestamp.py
|   |       |   |   |   |           __init__.py
|   |       |   |   |   |           
|   |       |   |   |   +---ranges
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_join.py
|   |       |   |   |   |       test_range.py
|   |       |   |   |   |       test_setops.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---string
|   |       |   |   |   |       test_astype.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---timedeltas
|   |       |   |   |       |   test_arithmetic.py
|   |       |   |   |       |   test_constructors.py
|   |       |   |   |       |   test_delete.py
|   |       |   |   |       |   test_formats.py
|   |       |   |   |       |   test_freq_attr.py
|   |       |   |   |       |   test_indexing.py
|   |       |   |   |       |   test_join.py
|   |       |   |   |       |   test_ops.py
|   |       |   |   |       |   test_pickle.py
|   |       |   |   |       |   test_scalar_compat.py
|   |       |   |   |       |   test_searchsorted.py
|   |       |   |   |       |   test_setops.py
|   |       |   |   |       |   test_timedelta.py
|   |       |   |   |       |   test_timedelta_range.py
|   |       |   |   |       |   __init__.py
|   |       |   |   |       |   
|   |       |   |   |       \---methods
|   |       |   |   |               test_astype.py
|   |       |   |   |               test_factorize.py
|   |       |   |   |               test_fillna.py
|   |       |   |   |               test_insert.py
|   |       |   |   |               test_repeat.py
|   |       |   |   |               test_shift.py
|   |       |   |   |               __init__.py
|   |       |   |   |               
|   |       |   |   +---indexing
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_at.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_chaining_and_caching.py
|   |       |   |   |   |   test_check_indexer.py
|   |       |   |   |   |   test_coercion.py
|   |       |   |   |   |   test_datetime.py
|   |       |   |   |   |   test_floats.py
|   |       |   |   |   |   test_iat.py
|   |       |   |   |   |   test_iloc.py
|   |       |   |   |   |   test_indexers.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_loc.py
|   |       |   |   |   |   test_na_indexing.py
|   |       |   |   |   |   test_partial.py
|   |       |   |   |   |   test_scalar.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---interval
|   |       |   |   |   |       test_interval.py
|   |       |   |   |   |       test_interval_new.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---multiindex
|   |       |   |   |           test_chaining_and_caching.py
|   |       |   |   |           test_datetime.py
|   |       |   |   |           test_getitem.py
|   |       |   |   |           test_iloc.py
|   |       |   |   |           test_indexing_slow.py
|   |       |   |   |           test_loc.py
|   |       |   |   |           test_multiindex.py
|   |       |   |   |           test_partial.py
|   |       |   |   |           test_setitem.py
|   |       |   |   |           test_slice.py
|   |       |   |   |           test_sorted.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---interchange
|   |       |   |   |       test_impl.py
|   |       |   |   |       test_spec_conformance.py
|   |       |   |   |       test_utils.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---internals
|   |       |   |   |       test_api.py
|   |       |   |   |       test_internals.py
|   |       |   |   |       test_managers.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---io
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   generate_legacy_storage_files.py
|   |       |   |   |   |   test_clipboard.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_compression.py
|   |       |   |   |   |   test_feather.py
|   |       |   |   |   |   test_fsspec.py
|   |       |   |   |   |   test_gbq.py
|   |       |   |   |   |   test_gcs.py
|   |       |   |   |   |   test_html.py
|   |       |   |   |   |   test_http_headers.py
|   |       |   |   |   |   test_orc.py
|   |       |   |   |   |   test_parquet.py
|   |       |   |   |   |   test_pickle.py
|   |       |   |   |   |   test_s3.py
|   |       |   |   |   |   test_spss.py
|   |       |   |   |   |   test_sql.py
|   |       |   |   |   |   test_stata.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---excel
|   |       |   |   |   |       test_odf.py
|   |       |   |   |   |       test_odswriter.py
|   |       |   |   |   |       test_openpyxl.py
|   |       |   |   |   |       test_readers.py
|   |       |   |   |   |       test_style.py
|   |       |   |   |   |       test_writers.py
|   |       |   |   |   |       test_xlrd.py
|   |       |   |   |   |       test_xlsxwriter.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---formats
|   |       |   |   |   |   |   test_console.py
|   |       |   |   |   |   |   test_css.py
|   |       |   |   |   |   |   test_eng_formatting.py
|   |       |   |   |   |   |   test_format.py
|   |       |   |   |   |   |   test_ipython_compat.py
|   |       |   |   |   |   |   test_printing.py
|   |       |   |   |   |   |   test_to_csv.py
|   |       |   |   |   |   |   test_to_excel.py
|   |       |   |   |   |   |   test_to_html.py
|   |       |   |   |   |   |   test_to_latex.py
|   |       |   |   |   |   |   test_to_markdown.py
|   |       |   |   |   |   |   test_to_string.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---style
|   |       |   |   |   |           test_bar.py
|   |       |   |   |   |           test_exceptions.py
|   |       |   |   |   |           test_format.py
|   |       |   |   |   |           test_highlight.py
|   |       |   |   |   |           test_html.py
|   |       |   |   |   |           test_matplotlib.py
|   |       |   |   |   |           test_non_unique.py
|   |       |   |   |   |           test_style.py
|   |       |   |   |   |           test_tooltip.py
|   |       |   |   |   |           test_to_latex.py
|   |       |   |   |   |           test_to_string.py
|   |       |   |   |   |           __init__.py
|   |       |   |   |   |           
|   |       |   |   |   +---json
|   |       |   |   |   |       conftest.py
|   |       |   |   |   |       test_compression.py
|   |       |   |   |   |       test_deprecated_kwargs.py
|   |       |   |   |   |       test_json_table_schema.py
|   |       |   |   |   |       test_json_table_schema_ext_dtype.py
|   |       |   |   |   |       test_normalize.py
|   |       |   |   |   |       test_pandas.py
|   |       |   |   |   |       test_readlines.py
|   |       |   |   |   |       test_ujson.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---parser
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_comment.py
|   |       |   |   |   |   |   test_compression.py
|   |       |   |   |   |   |   test_concatenate_chunks.py
|   |       |   |   |   |   |   test_converters.py
|   |       |   |   |   |   |   test_c_parser_only.py
|   |       |   |   |   |   |   test_dialect.py
|   |       |   |   |   |   |   test_encoding.py
|   |       |   |   |   |   |   test_header.py
|   |       |   |   |   |   |   test_index_col.py
|   |       |   |   |   |   |   test_mangle_dupes.py
|   |       |   |   |   |   |   test_multi_thread.py
|   |       |   |   |   |   |   test_na_values.py
|   |       |   |   |   |   |   test_network.py
|   |       |   |   |   |   |   test_parse_dates.py
|   |       |   |   |   |   |   test_python_parser_only.py
|   |       |   |   |   |   |   test_quoting.py
|   |       |   |   |   |   |   test_read_fwf.py
|   |       |   |   |   |   |   test_skiprows.py
|   |       |   |   |   |   |   test_textreader.py
|   |       |   |   |   |   |   test_unsupported.py
|   |       |   |   |   |   |   test_upcast.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---common
|   |       |   |   |   |   |       test_chunksize.py
|   |       |   |   |   |   |       test_common_basic.py
|   |       |   |   |   |   |       test_data_list.py
|   |       |   |   |   |   |       test_decimal.py
|   |       |   |   |   |   |       test_file_buffer_url.py
|   |       |   |   |   |   |       test_float.py
|   |       |   |   |   |   |       test_index.py
|   |       |   |   |   |   |       test_inf.py
|   |       |   |   |   |   |       test_ints.py
|   |       |   |   |   |   |       test_iterator.py
|   |       |   |   |   |   |       test_read_errors.py
|   |       |   |   |   |   |       test_verbose.py
|   |       |   |   |   |   |       __init__.py
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---dtypes
|   |       |   |   |   |   |       test_categorical.py
|   |       |   |   |   |   |       test_dtypes_basic.py
|   |       |   |   |   |   |       test_empty.py
|   |       |   |   |   |   |       __init__.py
|   |       |   |   |   |   |       
|   |       |   |   |   |   \---usecols
|   |       |   |   |   |           test_parse_dates.py
|   |       |   |   |   |           test_strings.py
|   |       |   |   |   |           test_usecols_basic.py
|   |       |   |   |   |           __init__.py
|   |       |   |   |   |           
|   |       |   |   |   +---pytables
|   |       |   |   |   |       common.py
|   |       |   |   |   |       conftest.py
|   |       |   |   |   |       test_append.py
|   |       |   |   |   |       test_categorical.py
|   |       |   |   |   |       test_compat.py
|   |       |   |   |   |       test_complex.py
|   |       |   |   |   |       test_errors.py
|   |       |   |   |   |       test_file_handling.py
|   |       |   |   |   |       test_keys.py
|   |       |   |   |   |       test_put.py
|   |       |   |   |   |       test_pytables_missing.py
|   |       |   |   |   |       test_read.py
|   |       |   |   |   |       test_retain_attributes.py
|   |       |   |   |   |       test_round_trip.py
|   |       |   |   |   |       test_select.py
|   |       |   |   |   |       test_store.py
|   |       |   |   |   |       test_subclass.py
|   |       |   |   |   |       test_timezones.py
|   |       |   |   |   |       test_time_series.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---sas
|   |       |   |   |   |       test_byteswap.py
|   |       |   |   |   |       test_sas.py
|   |       |   |   |   |       test_sas7bdat.py
|   |       |   |   |   |       test_xport.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---xml
|   |       |   |   |           conftest.py
|   |       |   |   |           test_to_xml.py
|   |       |   |   |           test_xml.py
|   |       |   |   |           test_xml_dtypes.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---libs
|   |       |   |   |       test_hashtable.py
|   |       |   |   |       test_join.py
|   |       |   |   |       test_lib.py
|   |       |   |   |       test_libalgos.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---plotting
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_backend.py
|   |       |   |   |   |   test_boxplot_method.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_converter.py
|   |       |   |   |   |   test_datetimelike.py
|   |       |   |   |   |   test_groupby.py
|   |       |   |   |   |   test_hist_method.py
|   |       |   |   |   |   test_misc.py
|   |       |   |   |   |   test_series.py
|   |       |   |   |   |   test_style.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---frame
|   |       |   |   |           test_frame.py
|   |       |   |   |           test_frame_color.py
|   |       |   |   |           test_frame_groupby.py
|   |       |   |   |           test_frame_legend.py
|   |       |   |   |           test_frame_subplots.py
|   |       |   |   |           test_hist_box_by.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---reductions
|   |       |   |   |       test_reductions.py
|   |       |   |   |       test_stat_reductions.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---resample
|   |       |   |   |       conftest.py
|   |       |   |   |       test_base.py
|   |       |   |   |       test_datetime_index.py
|   |       |   |   |       test_period_index.py
|   |       |   |   |       test_resampler_grouper.py
|   |       |   |   |       test_resample_api.py
|   |       |   |   |       test_timedelta.py
|   |       |   |   |       test_time_grouper.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---reshape
|   |       |   |   |   |   test_crosstab.py
|   |       |   |   |   |   test_cut.py
|   |       |   |   |   |   test_from_dummies.py
|   |       |   |   |   |   test_get_dummies.py
|   |       |   |   |   |   test_melt.py
|   |       |   |   |   |   test_pivot.py
|   |       |   |   |   |   test_pivot_multilevel.py
|   |       |   |   |   |   test_qcut.py
|   |       |   |   |   |   test_union_categoricals.py
|   |       |   |   |   |   test_util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---concat
|   |       |   |   |   |       conftest.py
|   |       |   |   |   |       test_append.py
|   |       |   |   |   |       test_append_common.py
|   |       |   |   |   |       test_categorical.py
|   |       |   |   |   |       test_concat.py
|   |       |   |   |   |       test_dataframe.py
|   |       |   |   |   |       test_datetimes.py
|   |       |   |   |   |       test_empty.py
|   |       |   |   |   |       test_index.py
|   |       |   |   |   |       test_invalid.py
|   |       |   |   |   |       test_series.py
|   |       |   |   |   |       test_sort.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---merge
|   |       |   |   |           test_join.py
|   |       |   |   |           test_merge.py
|   |       |   |   |           test_merge_asof.py
|   |       |   |   |           test_merge_cross.py
|   |       |   |   |           test_merge_index_as_string.py
|   |       |   |   |           test_merge_ordered.py
|   |       |   |   |           test_multi.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---scalar
|   |       |   |   |   |   test_nat.py
|   |       |   |   |   |   test_na_scalar.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---interval
|   |       |   |   |   |       test_arithmetic.py
|   |       |   |   |   |       test_constructors.py
|   |       |   |   |   |       test_contains.py
|   |       |   |   |   |       test_formats.py
|   |       |   |   |   |       test_interval.py
|   |       |   |   |   |       test_overlaps.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---period
|   |       |   |   |   |       test_arithmetic.py
|   |       |   |   |   |       test_asfreq.py
|   |       |   |   |   |       test_period.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---timedelta
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_timedelta.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---methods
|   |       |   |   |   |           test_as_unit.py
|   |       |   |   |   |           test_round.py
|   |       |   |   |   |           __init__.py
|   |       |   |   |   |           
|   |       |   |   |   \---timestamp
|   |       |   |   |       |   test_arithmetic.py
|   |       |   |   |       |   test_comparisons.py
|   |       |   |   |       |   test_constructors.py
|   |       |   |   |       |   test_formats.py
|   |       |   |   |       |   test_timestamp.py
|   |       |   |   |       |   test_timezones.py
|   |       |   |   |       |   __init__.py
|   |       |   |   |       |   
|   |       |   |   |       \---methods
|   |       |   |   |               test_as_unit.py
|   |       |   |   |               test_normalize.py
|   |       |   |   |               test_replace.py
|   |       |   |   |               test_round.py
|   |       |   |   |               test_timestamp_method.py
|   |       |   |   |               test_to_julian_date.py
|   |       |   |   |               test_to_pydatetime.py
|   |       |   |   |               test_tz_convert.py
|   |       |   |   |               test_tz_localize.py
|   |       |   |   |               __init__.py
|   |       |   |   |               
|   |       |   |   +---series
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_cumulative.py
|   |       |   |   |   |   test_formats.py
|   |       |   |   |   |   test_iteration.py
|   |       |   |   |   |   test_logical_ops.py
|   |       |   |   |   |   test_missing.py
|   |       |   |   |   |   test_npfuncs.py
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_subclass.py
|   |       |   |   |   |   test_ufunc.py
|   |       |   |   |   |   test_unary.py
|   |       |   |   |   |   test_validate.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---accessors
|   |       |   |   |   |       test_cat_accessor.py
|   |       |   |   |   |       test_dt_accessor.py
|   |       |   |   |   |       test_list_accessor.py
|   |       |   |   |   |       test_sparse_accessor.py
|   |       |   |   |   |       test_struct_accessor.py
|   |       |   |   |   |       test_str_accessor.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---indexing
|   |       |   |   |   |       test_datetime.py
|   |       |   |   |   |       test_delitem.py
|   |       |   |   |   |       test_get.py
|   |       |   |   |   |       test_getitem.py
|   |       |   |   |   |       test_indexing.py
|   |       |   |   |   |       test_mask.py
|   |       |   |   |   |       test_setitem.py
|   |       |   |   |   |       test_set_value.py
|   |       |   |   |   |       test_take.py
|   |       |   |   |   |       test_where.py
|   |       |   |   |   |       test_xs.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---methods
|   |       |   |   |           test_add_prefix_suffix.py
|   |       |   |   |           test_align.py
|   |       |   |   |           test_argsort.py
|   |       |   |   |           test_asof.py
|   |       |   |   |           test_astype.py
|   |       |   |   |           test_autocorr.py
|   |       |   |   |           test_between.py
|   |       |   |   |           test_case_when.py
|   |       |   |   |           test_clip.py
|   |       |   |   |           test_combine.py
|   |       |   |   |           test_combine_first.py
|   |       |   |   |           test_compare.py
|   |       |   |   |           test_convert_dtypes.py
|   |       |   |   |           test_copy.py
|   |       |   |   |           test_count.py
|   |       |   |   |           test_cov_corr.py
|   |       |   |   |           test_describe.py
|   |       |   |   |           test_diff.py
|   |       |   |   |           test_drop.py
|   |       |   |   |           test_dropna.py
|   |       |   |   |           test_drop_duplicates.py
|   |       |   |   |           test_dtypes.py
|   |       |   |   |           test_duplicated.py
|   |       |   |   |           test_equals.py
|   |       |   |   |           test_explode.py
|   |       |   |   |           test_fillna.py
|   |       |   |   |           test_get_numeric_data.py
|   |       |   |   |           test_head_tail.py
|   |       |   |   |           test_infer_objects.py
|   |       |   |   |           test_info.py
|   |       |   |   |           test_interpolate.py
|   |       |   |   |           test_isin.py
|   |       |   |   |           test_isna.py
|   |       |   |   |           test_is_monotonic.py
|   |       |   |   |           test_is_unique.py
|   |       |   |   |           test_item.py
|   |       |   |   |           test_map.py
|   |       |   |   |           test_matmul.py
|   |       |   |   |           test_nlargest.py
|   |       |   |   |           test_nunique.py
|   |       |   |   |           test_pct_change.py
|   |       |   |   |           test_pop.py
|   |       |   |   |           test_quantile.py
|   |       |   |   |           test_rank.py
|   |       |   |   |           test_reindex.py
|   |       |   |   |           test_reindex_like.py
|   |       |   |   |           test_rename.py
|   |       |   |   |           test_rename_axis.py
|   |       |   |   |           test_repeat.py
|   |       |   |   |           test_replace.py
|   |       |   |   |           test_reset_index.py
|   |       |   |   |           test_round.py
|   |       |   |   |           test_searchsorted.py
|   |       |   |   |           test_set_name.py
|   |       |   |   |           test_size.py
|   |       |   |   |           test_sort_index.py
|   |       |   |   |           test_sort_values.py
|   |       |   |   |           test_tolist.py
|   |       |   |   |           test_to_csv.py
|   |       |   |   |           test_to_dict.py
|   |       |   |   |           test_to_frame.py
|   |       |   |   |           test_to_numpy.py
|   |       |   |   |           test_truncate.py
|   |       |   |   |           test_tz_localize.py
|   |       |   |   |           test_unique.py
|   |       |   |   |           test_unstack.py
|   |       |   |   |           test_update.py
|   |       |   |   |           test_values.py
|   |       |   |   |           test_value_counts.py
|   |       |   |   |           test_view.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---strings
|   |       |   |   |       conftest.py
|   |       |   |   |       test_api.py
|   |       |   |   |       test_case_justify.py
|   |       |   |   |       test_cat.py
|   |       |   |   |       test_extract.py
|   |       |   |   |       test_find_replace.py
|   |       |   |   |       test_get_dummies.py
|   |       |   |   |       test_split_partition.py
|   |       |   |   |       test_strings.py
|   |       |   |   |       test_string_array.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---tools
|   |       |   |   |       test_to_datetime.py
|   |       |   |   |       test_to_numeric.py
|   |       |   |   |       test_to_time.py
|   |       |   |   |       test_to_timedelta.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---tseries
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---frequencies
|   |       |   |   |   |       test_frequencies.py
|   |       |   |   |   |       test_freq_code.py
|   |       |   |   |   |       test_inference.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   +---holiday
|   |       |   |   |   |       test_calendar.py
|   |       |   |   |   |       test_federal.py
|   |       |   |   |   |       test_holiday.py
|   |       |   |   |   |       test_observance.py
|   |       |   |   |   |       __init__.py
|   |       |   |   |   |       
|   |       |   |   |   \---offsets
|   |       |   |   |           common.py
|   |       |   |   |           test_business_day.py
|   |       |   |   |           test_business_hour.py
|   |       |   |   |           test_business_month.py
|   |       |   |   |           test_business_quarter.py
|   |       |   |   |           test_business_year.py
|   |       |   |   |           test_common.py
|   |       |   |   |           test_custom_business_day.py
|   |       |   |   |           test_custom_business_hour.py
|   |       |   |   |           test_custom_business_month.py
|   |       |   |   |           test_dst.py
|   |       |   |   |           test_easter.py
|   |       |   |   |           test_fiscal.py
|   |       |   |   |           test_index.py
|   |       |   |   |           test_month.py
|   |       |   |   |           test_offsets.py
|   |       |   |   |           test_offsets_properties.py
|   |       |   |   |           test_quarter.py
|   |       |   |   |           test_ticks.py
|   |       |   |   |           test_week.py
|   |       |   |   |           test_year.py
|   |       |   |   |           __init__.py
|   |       |   |   |           
|   |       |   |   +---tslibs
|   |       |   |   |       test_api.py
|   |       |   |   |       test_array_to_datetime.py
|   |       |   |   |       test_ccalendar.py
|   |       |   |   |       test_conversion.py
|   |       |   |   |       test_fields.py
|   |       |   |   |       test_libfrequencies.py
|   |       |   |   |       test_liboffsets.py
|   |       |   |   |       test_npy_units.py
|   |       |   |   |       test_np_datetime.py
|   |       |   |   |       test_parse_iso8601.py
|   |       |   |   |       test_parsing.py
|   |       |   |   |       test_period.py
|   |       |   |   |       test_resolution.py
|   |       |   |   |       test_strptime.py
|   |       |   |   |       test_timedeltas.py
|   |       |   |   |       test_timezones.py
|   |       |   |   |       test_to_offset.py
|   |       |   |   |       test_tzconversion.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---util
|   |       |   |   |       conftest.py
|   |       |   |   |       test_assert_almost_equal.py
|   |       |   |   |       test_assert_attr_equal.py
|   |       |   |   |       test_assert_categorical_equal.py
|   |       |   |   |       test_assert_extension_array_equal.py
|   |       |   |   |       test_assert_frame_equal.py
|   |       |   |   |       test_assert_index_equal.py
|   |       |   |   |       test_assert_interval_array_equal.py
|   |       |   |   |       test_assert_numpy_array_equal.py
|   |       |   |   |       test_assert_produces_warning.py
|   |       |   |   |       test_assert_series_equal.py
|   |       |   |   |       test_deprecate.py
|   |       |   |   |       test_deprecate_kwarg.py
|   |       |   |   |       test_deprecate_nonkeyword_arguments.py
|   |       |   |   |       test_doc.py
|   |       |   |   |       test_hashing.py
|   |       |   |   |       test_numba.py
|   |       |   |   |       test_rewrite_warning.py
|   |       |   |   |       test_shares_memory.py
|   |       |   |   |       test_show_versions.py
|   |       |   |   |       test_util.py
|   |       |   |   |       test_validate_args.py
|   |       |   |   |       test_validate_args_and_kwargs.py
|   |       |   |   |       test_validate_inclusive.py
|   |       |   |   |       test_validate_kwargs.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---window
|   |       |   |       |   conftest.py
|   |       |   |       |   test_api.py
|   |       |   |       |   test_apply.py
|   |       |   |       |   test_base_indexer.py
|   |       |   |       |   test_cython_aggregations.py
|   |       |   |       |   test_dtypes.py
|   |       |   |       |   test_ewm.py
|   |       |   |       |   test_expanding.py
|   |       |   |       |   test_groupby.py
|   |       |   |       |   test_numba.py
|   |       |   |       |   test_online.py
|   |       |   |       |   test_pairwise.py
|   |       |   |       |   test_rolling.py
|   |       |   |       |   test_rolling_functions.py
|   |       |   |       |   test_rolling_quantile.py
|   |       |   |       |   test_rolling_skew_kurt.py
|   |       |   |       |   test_timeseries_window.py
|   |       |   |       |   test_win_type.py
|   |       |   |       |   __init__.py
|   |       |   |       |   
|   |       |   |       \---moments
|   |       |   |               conftest.py
|   |       |   |               test_moments_consistency_ewm.py
|   |       |   |               test_moments_consistency_expanding.py
|   |       |   |               test_moments_consistency_rolling.py
|   |       |   |               __init__.py
|   |       |   |               
|   |       |   +---tseries
|   |       |   |   |   api.py
|   |       |   |   |   frequencies.py
|   |       |   |   |   holiday.py
|   |       |   |   |   offsets.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           api.cpython-312.pyc
|   |       |   |           frequencies.cpython-312.pyc
|   |       |   |           offsets.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---util
|   |       |   |   |   _decorators.py
|   |       |   |   |   _doctools.py
|   |       |   |   |   _exceptions.py
|   |       |   |   |   _print_versions.py
|   |       |   |   |   _tester.py
|   |       |   |   |   _test_decorators.py
|   |       |   |   |   _validators.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---version
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           _decorators.cpython-312.pyc
|   |       |   |           _exceptions.cpython-312.pyc
|   |       |   |           _print_versions.cpython-312.pyc
|   |       |   |           _tester.cpython-312.pyc
|   |       |   |           _validators.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---_config
|   |       |   |   |   config.py
|   |       |   |   |   dates.py
|   |       |   |   |   display.py
|   |       |   |   |   localization.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           config.cpython-312.pyc
|   |       |   |           dates.cpython-312.pyc
|   |       |   |           display.cpython-312.pyc
|   |       |   |           localization.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---_libs
|   |       |   |   |   algos.cp312-win_amd64.lib
|   |       |   |   |   algos.cp312-win_amd64.pyd
|   |       |   |   |   algos.pyi
|   |       |   |   |   arrays.cp312-win_amd64.lib
|   |       |   |   |   arrays.cp312-win_amd64.pyd
|   |       |   |   |   arrays.pyi
|   |       |   |   |   byteswap.cp312-win_amd64.lib
|   |       |   |   |   byteswap.cp312-win_amd64.pyd
|   |       |   |   |   byteswap.pyi
|   |       |   |   |   groupby.cp312-win_amd64.lib
|   |       |   |   |   groupby.cp312-win_amd64.pyd
|   |       |   |   |   groupby.pyi
|   |       |   |   |   hashing.cp312-win_amd64.lib
|   |       |   |   |   hashing.cp312-win_amd64.pyd
|   |       |   |   |   hashing.pyi
|   |       |   |   |   hashtable.cp312-win_amd64.lib
|   |       |   |   |   hashtable.cp312-win_amd64.pyd
|   |       |   |   |   hashtable.pyi
|   |       |   |   |   index.cp312-win_amd64.lib
|   |       |   |   |   index.cp312-win_amd64.pyd
|   |       |   |   |   index.pyi
|   |       |   |   |   indexing.cp312-win_amd64.lib
|   |       |   |   |   indexing.cp312-win_amd64.pyd
|   |       |   |   |   indexing.pyi
|   |       |   |   |   internals.cp312-win_amd64.lib
|   |       |   |   |   internals.cp312-win_amd64.pyd
|   |       |   |   |   internals.pyi
|   |       |   |   |   interval.cp312-win_amd64.lib
|   |       |   |   |   interval.cp312-win_amd64.pyd
|   |       |   |   |   interval.pyi
|   |       |   |   |   join.cp312-win_amd64.lib
|   |       |   |   |   join.cp312-win_amd64.pyd
|   |       |   |   |   join.pyi
|   |       |   |   |   json.cp312-win_amd64.lib
|   |       |   |   |   json.cp312-win_amd64.pyd
|   |       |   |   |   json.pyi
|   |       |   |   |   lib.cp312-win_amd64.lib
|   |       |   |   |   lib.cp312-win_amd64.pyd
|   |       |   |   |   lib.pyi
|   |       |   |   |   missing.cp312-win_amd64.lib
|   |       |   |   |   missing.cp312-win_amd64.pyd
|   |       |   |   |   missing.pyi
|   |       |   |   |   ops.cp312-win_amd64.lib
|   |       |   |   |   ops.cp312-win_amd64.pyd
|   |       |   |   |   ops.pyi
|   |       |   |   |   ops_dispatch.cp312-win_amd64.lib
|   |       |   |   |   ops_dispatch.cp312-win_amd64.pyd
|   |       |   |   |   ops_dispatch.pyi
|   |       |   |   |   pandas_datetime.cp312-win_amd64.lib
|   |       |   |   |   pandas_datetime.cp312-win_amd64.pyd
|   |       |   |   |   pandas_parser.cp312-win_amd64.lib
|   |       |   |   |   pandas_parser.cp312-win_amd64.pyd
|   |       |   |   |   parsers.cp312-win_amd64.lib
|   |       |   |   |   parsers.cp312-win_amd64.pyd
|   |       |   |   |   parsers.pyi
|   |       |   |   |   properties.cp312-win_amd64.lib
|   |       |   |   |   properties.cp312-win_amd64.pyd
|   |       |   |   |   properties.pyi
|   |       |   |   |   reshape.cp312-win_amd64.lib
|   |       |   |   |   reshape.cp312-win_amd64.pyd
|   |       |   |   |   reshape.pyi
|   |       |   |   |   sas.cp312-win_amd64.lib
|   |       |   |   |   sas.cp312-win_amd64.pyd
|   |       |   |   |   sas.pyi
|   |       |   |   |   sparse.cp312-win_amd64.lib
|   |       |   |   |   sparse.cp312-win_amd64.pyd
|   |       |   |   |   sparse.pyi
|   |       |   |   |   testing.cp312-win_amd64.lib
|   |       |   |   |   testing.cp312-win_amd64.pyd
|   |       |   |   |   testing.pyi
|   |       |   |   |   tslib.cp312-win_amd64.lib
|   |       |   |   |   tslib.cp312-win_amd64.pyd
|   |       |   |   |   tslib.pyi
|   |       |   |   |   writers.cp312-win_amd64.lib
|   |       |   |   |   writers.cp312-win_amd64.pyd
|   |       |   |   |   writers.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---tslibs
|   |       |   |   |   |   base.cp312-win_amd64.lib
|   |       |   |   |   |   base.cp312-win_amd64.pyd
|   |       |   |   |   |   ccalendar.cp312-win_amd64.lib
|   |       |   |   |   |   ccalendar.cp312-win_amd64.pyd
|   |       |   |   |   |   ccalendar.pyi
|   |       |   |   |   |   conversion.cp312-win_amd64.lib
|   |       |   |   |   |   conversion.cp312-win_amd64.pyd
|   |       |   |   |   |   conversion.pyi
|   |       |   |   |   |   dtypes.cp312-win_amd64.lib
|   |       |   |   |   |   dtypes.cp312-win_amd64.pyd
|   |       |   |   |   |   dtypes.pyi
|   |       |   |   |   |   fields.cp312-win_amd64.lib
|   |       |   |   |   |   fields.cp312-win_amd64.pyd
|   |       |   |   |   |   fields.pyi
|   |       |   |   |   |   nattype.cp312-win_amd64.lib
|   |       |   |   |   |   nattype.cp312-win_amd64.pyd
|   |       |   |   |   |   nattype.pyi
|   |       |   |   |   |   np_datetime.cp312-win_amd64.lib
|   |       |   |   |   |   np_datetime.cp312-win_amd64.pyd
|   |       |   |   |   |   np_datetime.pyi
|   |       |   |   |   |   offsets.cp312-win_amd64.lib
|   |       |   |   |   |   offsets.cp312-win_amd64.pyd
|   |       |   |   |   |   offsets.pyi
|   |       |   |   |   |   parsing.cp312-win_amd64.lib
|   |       |   |   |   |   parsing.cp312-win_amd64.pyd
|   |       |   |   |   |   parsing.pyi
|   |       |   |   |   |   period.cp312-win_amd64.lib
|   |       |   |   |   |   period.cp312-win_amd64.pyd
|   |       |   |   |   |   period.pyi
|   |       |   |   |   |   strptime.cp312-win_amd64.lib
|   |       |   |   |   |   strptime.cp312-win_amd64.pyd
|   |       |   |   |   |   strptime.pyi
|   |       |   |   |   |   timedeltas.cp312-win_amd64.lib
|   |       |   |   |   |   timedeltas.cp312-win_amd64.pyd
|   |       |   |   |   |   timedeltas.pyi
|   |       |   |   |   |   timestamps.cp312-win_amd64.lib
|   |       |   |   |   |   timestamps.cp312-win_amd64.pyd
|   |       |   |   |   |   timestamps.pyi
|   |       |   |   |   |   timezones.cp312-win_amd64.lib
|   |       |   |   |   |   timezones.cp312-win_amd64.pyd
|   |       |   |   |   |   timezones.pyi
|   |       |   |   |   |   tzconversion.cp312-win_amd64.lib
|   |       |   |   |   |   tzconversion.cp312-win_amd64.pyd
|   |       |   |   |   |   tzconversion.pyi
|   |       |   |   |   |   vectorized.cp312-win_amd64.lib
|   |       |   |   |   |   vectorized.cp312-win_amd64.pyd
|   |       |   |   |   |   vectorized.pyi
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   +---window
|   |       |   |   |   |   aggregations.cp312-win_amd64.lib
|   |       |   |   |   |   aggregations.cp312-win_amd64.pyd
|   |       |   |   |   |   aggregations.pyi
|   |       |   |   |   |   indexers.cp312-win_amd64.lib
|   |       |   |   |   |   indexers.cp312-win_amd64.pyd
|   |       |   |   |   |   indexers.pyi
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-312.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---_testing
|   |       |   |   |   asserters.py
|   |       |   |   |   compat.py
|   |       |   |   |   contexts.py
|   |       |   |   |   _hypothesis.py
|   |       |   |   |   _io.py
|   |       |   |   |   _warnings.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           asserters.cpython-312.pyc
|   |       |   |           compat.cpython-312.pyc
|   |       |   |           contexts.cpython-312.pyc
|   |       |   |           _io.cpython-312.pyc
|   |       |   |           _warnings.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           testing.cpython-312.pyc
|   |       |           _typing.cpython-312.pyc
|   |       |           _version_meson.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---pandas-2.3.2.dist-info
|   |       |       DELVEWHEEL
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---pandas.libs
|   |       |       msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|   |       |       
|   |       +---PIL
|   |       |   |   AvifImagePlugin.py
|   |       |   |   BdfFontFile.py
|   |       |   |   BlpImagePlugin.py
|   |       |   |   BmpImagePlugin.py
|   |       |   |   BufrStubImagePlugin.py
|   |       |   |   ContainerIO.py
|   |       |   |   CurImagePlugin.py
|   |       |   |   DcxImagePlugin.py
|   |       |   |   DdsImagePlugin.py
|   |       |   |   EpsImagePlugin.py
|   |       |   |   ExifTags.py
|   |       |   |   features.py
|   |       |   |   FitsImagePlugin.py
|   |       |   |   FliImagePlugin.py
|   |       |   |   FontFile.py
|   |       |   |   FpxImagePlugin.py
|   |       |   |   FtexImagePlugin.py
|   |       |   |   GbrImagePlugin.py
|   |       |   |   GdImageFile.py
|   |       |   |   GifImagePlugin.py
|   |       |   |   GimpGradientFile.py
|   |       |   |   GimpPaletteFile.py
|   |       |   |   GribStubImagePlugin.py
|   |       |   |   Hdf5StubImagePlugin.py
|   |       |   |   IcnsImagePlugin.py
|   |       |   |   IcoImagePlugin.py
|   |       |   |   Image.py
|   |       |   |   ImageChops.py
|   |       |   |   ImageCms.py
|   |       |   |   ImageColor.py
|   |       |   |   ImageDraw.py
|   |       |   |   ImageDraw2.py
|   |       |   |   ImageEnhance.py
|   |       |   |   ImageFile.py
|   |       |   |   ImageFilter.py
|   |       |   |   ImageFont.py
|   |       |   |   ImageGrab.py
|   |       |   |   ImageMath.py
|   |       |   |   ImageMode.py
|   |       |   |   ImageMorph.py
|   |       |   |   ImageOps.py
|   |       |   |   ImagePalette.py
|   |       |   |   ImagePath.py
|   |       |   |   ImageQt.py
|   |       |   |   ImageSequence.py
|   |       |   |   ImageShow.py
|   |       |   |   ImageStat.py
|   |       |   |   ImageTk.py
|   |       |   |   ImageTransform.py
|   |       |   |   ImageWin.py
|   |       |   |   ImImagePlugin.py
|   |       |   |   ImtImagePlugin.py
|   |       |   |   IptcImagePlugin.py
|   |       |   |   Jpeg2KImagePlugin.py
|   |       |   |   JpegImagePlugin.py
|   |       |   |   JpegPresets.py
|   |       |   |   McIdasImagePlugin.py
|   |       |   |   MicImagePlugin.py
|   |       |   |   MpegImagePlugin.py
|   |       |   |   MpoImagePlugin.py
|   |       |   |   MspImagePlugin.py
|   |       |   |   PaletteFile.py
|   |       |   |   PalmImagePlugin.py
|   |       |   |   PcdImagePlugin.py
|   |       |   |   PcfFontFile.py
|   |       |   |   PcxImagePlugin.py
|   |       |   |   PdfImagePlugin.py
|   |       |   |   PdfParser.py
|   |       |   |   PixarImagePlugin.py
|   |       |   |   PngImagePlugin.py
|   |       |   |   PpmImagePlugin.py
|   |       |   |   PsdImagePlugin.py
|   |       |   |   PSDraw.py
|   |       |   |   py.typed
|   |       |   |   QoiImagePlugin.py
|   |       |   |   report.py
|   |       |   |   SgiImagePlugin.py
|   |       |   |   SpiderImagePlugin.py
|   |       |   |   SunImagePlugin.py
|   |       |   |   TarIO.py
|   |       |   |   TgaImagePlugin.py
|   |       |   |   TiffImagePlugin.py
|   |       |   |   TiffTags.py
|   |       |   |   WalImageFile.py
|   |       |   |   WebPImagePlugin.py
|   |       |   |   WmfImagePlugin.py
|   |       |   |   XbmImagePlugin.py
|   |       |   |   XpmImagePlugin.py
|   |       |   |   XVThumbImagePlugin.py
|   |       |   |   _avif.cp312-win_amd64.pyd
|   |       |   |   _avif.pyi
|   |       |   |   _binary.py
|   |       |   |   _deprecate.py
|   |       |   |   _imaging.cp312-win_amd64.pyd
|   |       |   |   _imaging.pyi
|   |       |   |   _imagingcms.cp312-win_amd64.pyd
|   |       |   |   _imagingcms.pyi
|   |       |   |   _imagingft.cp312-win_amd64.pyd
|   |       |   |   _imagingft.pyi
|   |       |   |   _imagingmath.cp312-win_amd64.pyd
|   |       |   |   _imagingmath.pyi
|   |       |   |   _imagingmorph.cp312-win_amd64.pyd
|   |       |   |   _imagingmorph.pyi
|   |       |   |   _imagingtk.cp312-win_amd64.pyd
|   |       |   |   _imagingtk.pyi
|   |       |   |   _tkinter_finder.py
|   |       |   |   _typing.py
|   |       |   |   _util.py
|   |       |   |   _version.py
|   |       |   |   _webp.cp312-win_amd64.pyd
|   |       |   |   _webp.pyi
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           ExifTags.cpython-312.pyc
|   |       |           GimpGradientFile.cpython-312.pyc
|   |       |           GimpPaletteFile.cpython-312.pyc
|   |       |           Image.cpython-312.pyc
|   |       |           ImageChops.cpython-312.pyc
|   |       |           ImageColor.cpython-312.pyc
|   |       |           ImageFile.cpython-312.pyc
|   |       |           ImageMode.cpython-312.pyc
|   |       |           ImagePalette.cpython-312.pyc
|   |       |           ImageSequence.cpython-312.pyc
|   |       |           PaletteFile.cpython-312.pyc
|   |       |           PngImagePlugin.cpython-312.pyc
|   |       |           TiffTags.cpython-312.pyc
|   |       |           _binary.cpython-312.pyc
|   |       |           _deprecate.cpython-312.pyc
|   |       |           _typing.cpython-312.pyc
|   |       |           _util.cpython-312.pyc
|   |       |           _version.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---pillow-11.3.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   zip-safe
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pyparsing
|   |       |   |   actions.py
|   |       |   |   common.py
|   |       |   |   core.py
|   |       |   |   exceptions.py
|   |       |   |   helpers.py
|   |       |   |   py.typed
|   |       |   |   results.py
|   |       |   |   testing.py
|   |       |   |   unicode.py
|   |       |   |   util.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---diagram
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   +---tools
|   |       |   |       cvt_pyparsing_pep8_names.py
|   |       |   |       __init__.py
|   |       |   |       
|   |       |   \---__pycache__
|   |       |           actions.cpython-312.pyc
|   |       |           common.cpython-312.pyc
|   |       |           core.cpython-312.pyc
|   |       |           exceptions.cpython-312.pyc
|   |       |           helpers.cpython-312.pyc
|   |       |           results.cpython-312.pyc
|   |       |           testing.cpython-312.pyc
|   |       |           unicode.cpython-312.pyc
|   |       |           util.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---pyparsing-3.2.3.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---PyQt5
|   |       |   |   py.typed
|   |       |   |   pylupdate.pyd
|   |       |   |   pylupdate_main.py
|   |       |   |   pyrcc.pyd
|   |       |   |   pyrcc_main.py
|   |       |   |   QAxContainer.pyd
|   |       |   |   QAxContainer.pyi
|   |       |   |   Qt.pyd
|   |       |   |   QtBluetooth.pyd
|   |       |   |   QtBluetooth.pyi
|   |       |   |   QtCore.pyd
|   |       |   |   QtCore.pyi
|   |       |   |   QtDBus.pyd
|   |       |   |   QtDBus.pyi
|   |       |   |   QtDesigner.pyd
|   |       |   |   QtDesigner.pyi
|   |       |   |   QtGui.pyd
|   |       |   |   QtGui.pyi
|   |       |   |   QtHelp.pyd
|   |       |   |   QtHelp.pyi
|   |       |   |   QtLocation.pyd
|   |       |   |   QtLocation.pyi
|   |       |   |   QtMultimedia.pyd
|   |       |   |   QtMultimedia.pyi
|   |       |   |   QtMultimediaWidgets.pyd
|   |       |   |   QtMultimediaWidgets.pyi
|   |       |   |   QtNetwork.pyd
|   |       |   |   QtNetwork.pyi
|   |       |   |   QtNfc.pyd
|   |       |   |   QtNfc.pyi
|   |       |   |   QtOpenGL.pyd
|   |       |   |   QtOpenGL.pyi
|   |       |   |   QtPositioning.pyd
|   |       |   |   QtPositioning.pyi
|   |       |   |   QtPrintSupport.pyd
|   |       |   |   QtPrintSupport.pyi
|   |       |   |   QtQml.pyd
|   |       |   |   QtQml.pyi
|   |       |   |   QtQuick.pyd
|   |       |   |   QtQuick.pyi
|   |       |   |   QtQuick3D.pyd
|   |       |   |   QtQuick3D.pyi
|   |       |   |   QtQuickWidgets.pyd
|   |       |   |   QtQuickWidgets.pyi
|   |       |   |   QtRemoteObjects.pyd
|   |       |   |   QtRemoteObjects.pyi
|   |       |   |   QtSensors.pyd
|   |       |   |   QtSensors.pyi
|   |       |   |   QtSerialPort.pyd
|   |       |   |   QtSerialPort.pyi
|   |       |   |   QtSql.pyd
|   |       |   |   QtSql.pyi
|   |       |   |   QtSvg.pyd
|   |       |   |   QtSvg.pyi
|   |       |   |   QtTest.pyd
|   |       |   |   QtTest.pyi
|   |       |   |   QtTextToSpeech.pyd
|   |       |   |   QtTextToSpeech.pyi
|   |       |   |   QtWebChannel.pyd
|   |       |   |   QtWebChannel.pyi
|   |       |   |   QtWebSockets.pyd
|   |       |   |   QtWebSockets.pyi
|   |       |   |   QtWidgets.pyd
|   |       |   |   QtWidgets.pyi
|   |       |   |   QtWinExtras.pyd
|   |       |   |   QtWinExtras.pyi
|   |       |   |   QtXml.pyd
|   |       |   |   QtXml.pyi
|   |       |   |   QtXmlPatterns.pyd
|   |       |   |   QtXmlPatterns.pyi
|   |       |   |   sip.cp312-win_amd64.pyd
|   |       |   |   sip.pyi
|   |       |   |   _QOpenGLFunctions_2_0.pyd
|   |       |   |   _QOpenGLFunctions_2_1.pyd
|   |       |   |   _QOpenGLFunctions_4_1_Core.pyd
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---bindings
|   |       |   |   +---QAxContainer
|   |       |   |   |       qaxbase.sip
|   |       |   |   |       QAxContainer.toml
|   |       |   |   |       QAxContainermod.sip
|   |       |   |   |       qaxobject.sip
|   |       |   |   |       qaxwidget.sip
|   |       |   |   |       
|   |       |   |   +---QtBluetooth
|   |       |   |   |       qbluetooth.sip
|   |       |   |   |       qbluetoothaddress.sip
|   |       |   |   |       qbluetoothdevicediscoveryagent.sip
|   |       |   |   |       qbluetoothdeviceinfo.sip
|   |       |   |   |       qbluetoothhostinfo.sip
|   |       |   |   |       qbluetoothlocaldevice.sip
|   |       |   |   |       qbluetoothserver.sip
|   |       |   |   |       qbluetoothservicediscoveryagent.sip
|   |       |   |   |       qbluetoothserviceinfo.sip
|   |       |   |   |       qbluetoothsocket.sip
|   |       |   |   |       qbluetoothtransfermanager.sip
|   |       |   |   |       qbluetoothtransferreply.sip
|   |       |   |   |       qbluetoothtransferrequest.sip
|   |       |   |   |       qbluetoothuuid.sip
|   |       |   |   |       qlowenergyadvertisingdata.sip
|   |       |   |   |       qlowenergyadvertisingparameters.sip
|   |       |   |   |       qlowenergycharacteristic.sip
|   |       |   |   |       qlowenergycharacteristicdata.sip
|   |       |   |   |       qlowenergyconnectionparameters.sip
|   |       |   |   |       qlowenergycontroller.sip
|   |       |   |   |       qlowenergydescriptor.sip
|   |       |   |   |       qlowenergydescriptordata.sip
|   |       |   |   |       qlowenergyservice.sip
|   |       |   |   |       qlowenergyservicedata.sip
|   |       |   |   |       qpybluetooth_qlist.sip
|   |       |   |   |       qpybluetooth_quint128.sip
|   |       |   |   |       QtBluetooth.toml
|   |       |   |   |       QtBluetoothmod.sip
|   |       |   |   |       
|   |       |   |   +---QtCore
|   |       |   |   |       pyqt-gpl.sip5
|   |       |   |   |       qabstractanimation.sip
|   |       |   |   |       qabstracteventdispatcher.sip
|   |       |   |   |       qabstractitemmodel.sip
|   |       |   |   |       qabstractnativeeventfilter.sip
|   |       |   |   |       qabstractproxymodel.sip
|   |       |   |   |       qabstractstate.sip
|   |       |   |   |       qabstracttransition.sip
|   |       |   |   |       qanimationgroup.sip
|   |       |   |   |       qbasictimer.sip
|   |       |   |   |       qbitarray.sip
|   |       |   |   |       qbuffer.sip
|   |       |   |   |       qbytearray.sip
|   |       |   |   |       qbytearraymatcher.sip
|   |       |   |   |       qcalendar.sip
|   |       |   |   |       qcborcommon.sip
|   |       |   |   |       qcborstream.sip
|   |       |   |   |       qchar.sip
|   |       |   |   |       qcollator.sip
|   |       |   |   |       qcommandlineoption.sip
|   |       |   |   |       qcommandlineparser.sip
|   |       |   |   |       qconcatenatetablesproxymodel.sip
|   |       |   |   |       qcoreapplication.sip
|   |       |   |   |       qcoreevent.sip
|   |       |   |   |       qcryptographichash.sip
|   |       |   |   |       qdatastream.sip
|   |       |   |   |       qdatetime.sip
|   |       |   |   |       qdeadlinetimer.sip
|   |       |   |   |       qdir.sip
|   |       |   |   |       qdiriterator.sip
|   |       |   |   |       qeasingcurve.sip
|   |       |   |   |       qelapsedtimer.sip
|   |       |   |   |       qeventloop.sip
|   |       |   |   |       qeventtransition.sip
|   |       |   |   |       qfile.sip
|   |       |   |   |       qfiledevice.sip
|   |       |   |   |       qfileinfo.sip
|   |       |   |   |       qfileselector.sip
|   |       |   |   |       qfilesystemwatcher.sip
|   |       |   |   |       qfinalstate.sip
|   |       |   |   |       qglobal.sip
|   |       |   |   |       qhistorystate.sip
|   |       |   |   |       qidentityproxymodel.sip
|   |       |   |   |       qiodevice.sip
|   |       |   |   |       qitemselectionmodel.sip
|   |       |   |   |       qjsonarray.sip
|   |       |   |   |       qjsondocument.sip
|   |       |   |   |       qjsonobject.sip
|   |       |   |   |       qjsonvalue.sip
|   |       |   |   |       qlibrary.sip
|   |       |   |   |       qlibraryinfo.sip
|   |       |   |   |       qline.sip
|   |       |   |   |       qlocale.sip
|   |       |   |   |       qlockfile.sip
|   |       |   |   |       qlogging.sip
|   |       |   |   |       qloggingcategory.sip
|   |       |   |   |       qmargins.sip
|   |       |   |   |       qmessageauthenticationcode.sip
|   |       |   |   |       qmetaobject.sip
|   |       |   |   |       qmetatype.sip
|   |       |   |   |       qmimedata.sip
|   |       |   |   |       qmimedatabase.sip
|   |       |   |   |       qmimetype.sip
|   |       |   |   |       qmutex.sip
|   |       |   |   |       qnamespace.sip
|   |       |   |   |       qnumeric.sip
|   |       |   |   |       qobject.sip
|   |       |   |   |       qobjectcleanuphandler.sip
|   |       |   |   |       qobjectdefs.sip
|   |       |   |   |       qoperatingsystemversion.sip
|   |       |   |   |       qparallelanimationgroup.sip
|   |       |   |   |       qpauseanimation.sip
|   |       |   |   |       qpluginloader.sip
|   |       |   |   |       qpoint.sip
|   |       |   |   |       qprocess.sip
|   |       |   |   |       qpropertyanimation.sip
|   |       |   |   |       qpycore_qhash.sip
|   |       |   |   |       qpycore_qlist.sip
|   |       |   |   |       qpycore_qmap.sip
|   |       |   |   |       qpycore_qpair.sip
|   |       |   |   |       qpycore_qset.sip
|   |       |   |   |       qpycore_qvariantmap.sip
|   |       |   |   |       qpycore_qvector.sip
|   |       |   |   |       qpycore_virtual_error_handler.sip
|   |       |   |   |       qrandom.sip
|   |       |   |   |       qreadwritelock.sip
|   |       |   |   |       qrect.sip
|   |       |   |   |       qregexp.sip
|   |       |   |   |       qregularexpression.sip
|   |       |   |   |       qresource.sip
|   |       |   |   |       qrunnable.sip
|   |       |   |   |       qsavefile.sip
|   |       |   |   |       qsemaphore.sip
|   |       |   |   |       qsequentialanimationgroup.sip
|   |       |   |   |       qsettings.sip
|   |       |   |   |       qsharedmemory.sip
|   |       |   |   |       qsignalmapper.sip
|   |       |   |   |       qsignaltransition.sip
|   |       |   |   |       qsize.sip
|   |       |   |   |       qsocketnotifier.sip
|   |       |   |   |       qsortfilterproxymodel.sip
|   |       |   |   |       qstandardpaths.sip
|   |       |   |   |       qstate.sip
|   |       |   |   |       qstatemachine.sip
|   |       |   |   |       qstorageinfo.sip
|   |       |   |   |       qstring.sip
|   |       |   |   |       qstringlist.sip
|   |       |   |   |       qstringlistmodel.sip
|   |       |   |   |       qsysinfo.sip
|   |       |   |   |       qsystemsemaphore.sip
|   |       |   |   |       QtCore.toml
|   |       |   |   |       QtCoremod.sip
|   |       |   |   |       qtemporarydir.sip
|   |       |   |   |       qtemporaryfile.sip
|   |       |   |   |       qtextboundaryfinder.sip
|   |       |   |   |       qtextcodec.sip
|   |       |   |   |       qtextstream.sip
|   |       |   |   |       qthread.sip
|   |       |   |   |       qthreadpool.sip
|   |       |   |   |       qtimeline.sip
|   |       |   |   |       qtimer.sip
|   |       |   |   |       qtimezone.sip
|   |       |   |   |       qtranslator.sip
|   |       |   |   |       qtransposeproxymodel.sip
|   |       |   |   |       qurl.sip
|   |       |   |   |       qurlquery.sip
|   |       |   |   |       quuid.sip
|   |       |   |   |       qvariant.sip
|   |       |   |   |       qvariantanimation.sip
|   |       |   |   |       qversionnumber.sip
|   |       |   |   |       qwaitcondition.sip
|   |       |   |   |       qwineventnotifier.sip
|   |       |   |   |       qxmlstream.sip
|   |       |   |   |       
|   |       |   |   +---QtDBus
|   |       |   |   |       qdbusabstractadaptor.sip
|   |       |   |   |       qdbusabstractinterface.sip
|   |       |   |   |       qdbusargument.sip
|   |       |   |   |       qdbusconnection.sip
|   |       |   |   |       qdbusconnectioninterface.sip
|   |       |   |   |       qdbuserror.sip
|   |       |   |   |       qdbusextratypes.sip
|   |       |   |   |       qdbusinterface.sip
|   |       |   |   |       qdbusmessage.sip
|   |       |   |   |       qdbuspendingcall.sip
|   |       |   |   |       qdbusservicewatcher.sip
|   |       |   |   |       qdbusunixfiledescriptor.sip
|   |       |   |   |       qpydbuspendingreply.sip
|   |       |   |   |       qpydbusreply.sip
|   |       |   |   |       QtDBus.toml
|   |       |   |   |       QtDBusmod.sip
|   |       |   |   |       
|   |       |   |   +---QtDesigner
|   |       |   |   |       abstractactioneditor.sip
|   |       |   |   |       abstractformbuilder.sip
|   |       |   |   |       abstractformeditor.sip
|   |       |   |   |       abstractformwindow.sip
|   |       |   |   |       abstractformwindowcursor.sip
|   |       |   |   |       abstractformwindowmanager.sip
|   |       |   |   |       abstractobjectinspector.sip
|   |       |   |   |       abstractpropertyeditor.sip
|   |       |   |   |       abstractwidgetbox.sip
|   |       |   |   |       container.sip
|   |       |   |   |       customwidget.sip
|   |       |   |   |       default_extensionfactory.sip
|   |       |   |   |       extension.sip
|   |       |   |   |       formbuilder.sip
|   |       |   |   |       membersheet.sip
|   |       |   |   |       propertysheet.sip
|   |       |   |   |       qextensionmanager.sip
|   |       |   |   |       qpydesignercontainerextension.sip
|   |       |   |   |       qpydesignercustomwidgetcollectionplugin.sip
|   |       |   |   |       qpydesignercustomwidgetplugin.sip
|   |       |   |   |       qpydesignermembersheetextension.sip
|   |       |   |   |       qpydesignerpropertysheetextension.sip
|   |       |   |   |       qpydesignertaskmenuextension.sip
|   |       |   |   |       QtDesigner.toml
|   |       |   |   |       QtDesignermod.sip
|   |       |   |   |       taskmenu.sip
|   |       |   |   |       
|   |       |   |   +---QtGui
|   |       |   |   |       opengl_types.sip
|   |       |   |   |       qabstracttextdocumentlayout.sip
|   |       |   |   |       qbackingstore.sip
|   |       |   |   |       qbitmap.sip
|   |       |   |   |       qbrush.sip
|   |       |   |   |       qclipboard.sip
|   |       |   |   |       qcolor.sip
|   |       |   |   |       qcolorspace.sip
|   |       |   |   |       qcolortransform.sip
|   |       |   |   |       qcursor.sip
|   |       |   |   |       qdesktopservices.sip
|   |       |   |   |       qdrag.sip
|   |       |   |   |       qevent.sip
|   |       |   |   |       qfont.sip
|   |       |   |   |       qfontdatabase.sip
|   |       |   |   |       qfontinfo.sip
|   |       |   |   |       qfontmetrics.sip
|   |       |   |   |       qgenericmatrix.sip
|   |       |   |   |       qglyphrun.sip
|   |       |   |   |       qguiapplication.sip
|   |       |   |   |       qicon.sip
|   |       |   |   |       qiconengine.sip
|   |       |   |   |       qimage.sip
|   |       |   |   |       qimageiohandler.sip
|   |       |   |   |       qimagereader.sip
|   |       |   |   |       qimagewriter.sip
|   |       |   |   |       qinputmethod.sip
|   |       |   |   |       qkeysequence.sip
|   |       |   |   |       qmatrix4x4.sip
|   |       |   |   |       qmovie.sip
|   |       |   |   |       qoffscreensurface.sip
|   |       |   |   |       qopenglbuffer.sip
|   |       |   |   |       qopenglcontext.sip
|   |       |   |   |       qopengldebug.sip
|   |       |   |   |       qopenglframebufferobject.sip
|   |       |   |   |       qopenglpaintdevice.sip
|   |       |   |   |       qopenglpixeltransferoptions.sip
|   |       |   |   |       qopenglshaderprogram.sip
|   |       |   |   |       qopengltexture.sip
|   |       |   |   |       qopengltextureblitter.sip
|   |       |   |   |       qopengltimerquery.sip
|   |       |   |   |       qopenglversionfunctions.sip
|   |       |   |   |       qopenglvertexarrayobject.sip
|   |       |   |   |       qopenglwindow.sip
|   |       |   |   |       qpagedpaintdevice.sip
|   |       |   |   |       qpagelayout.sip
|   |       |   |   |       qpagesize.sip
|   |       |   |   |       qpaintdevice.sip
|   |       |   |   |       qpaintdevicewindow.sip
|   |       |   |   |       qpaintengine.sip
|   |       |   |   |       qpainter.sip
|   |       |   |   |       qpainterpath.sip
|   |       |   |   |       qpalette.sip
|   |       |   |   |       qpdfwriter.sip
|   |       |   |   |       qpen.sip
|   |       |   |   |       qpicture.sip
|   |       |   |   |       qpixelformat.sip
|   |       |   |   |       qpixmap.sip
|   |       |   |   |       qpixmapcache.sip
|   |       |   |   |       qpolygon.sip
|   |       |   |   |       qpygui_qlist.sip
|   |       |   |   |       qpygui_qpair.sip
|   |       |   |   |       qpygui_qvector.sip
|   |       |   |   |       qquaternion.sip
|   |       |   |   |       qrasterwindow.sip
|   |       |   |   |       qrawfont.sip
|   |       |   |   |       qregion.sip
|   |       |   |   |       qrgb.sip
|   |       |   |   |       qrgba64.sip
|   |       |   |   |       qscreen.sip
|   |       |   |   |       qsessionmanager.sip
|   |       |   |   |       qstandarditemmodel.sip
|   |       |   |   |       qstatictext.sip
|   |       |   |   |       qstylehints.sip
|   |       |   |   |       qsurface.sip
|   |       |   |   |       qsurfaceformat.sip
|   |       |   |   |       qsyntaxhighlighter.sip
|   |       |   |   |       qtextcursor.sip
|   |       |   |   |       qtextdocument.sip
|   |       |   |   |       qtextdocumentfragment.sip
|   |       |   |   |       qtextdocumentwriter.sip
|   |       |   |   |       qtextformat.sip
|   |       |   |   |       qtextlayout.sip
|   |       |   |   |       qtextlist.sip
|   |       |   |   |       qtextobject.sip
|   |       |   |   |       qtextoption.sip
|   |       |   |   |       qtexttable.sip
|   |       |   |   |       QtGui.toml
|   |       |   |   |       QtGuimod.sip
|   |       |   |   |       qtouchdevice.sip
|   |       |   |   |       qtransform.sip
|   |       |   |   |       qvalidator.sip
|   |       |   |   |       qvector2d.sip
|   |       |   |   |       qvector3d.sip
|   |       |   |   |       qvector4d.sip
|   |       |   |   |       qwindow.sip
|   |       |   |   |       qwindowdefs.sip
|   |       |   |   |       
|   |       |   |   +---QtHelp
|   |       |   |   |       qcompressedhelpinfo.sip
|   |       |   |   |       qhelpcontentwidget.sip
|   |       |   |   |       qhelpengine.sip
|   |       |   |   |       qhelpenginecore.sip
|   |       |   |   |       qhelpfilterdata.sip
|   |       |   |   |       qhelpfilterengine.sip
|   |       |   |   |       qhelpfiltersettingswidget.sip
|   |       |   |   |       qhelpindexwidget.sip
|   |       |   |   |       qhelplink.sip
|   |       |   |   |       qhelpsearchengine.sip
|   |       |   |   |       qhelpsearchquerywidget.sip
|   |       |   |   |       qhelpsearchresultwidget.sip
|   |       |   |   |       QtHelp.toml
|   |       |   |   |       QtHelpmod.sip
|   |       |   |   |       
|   |       |   |   +---QtLocation
|   |       |   |   |       qgeocodereply.sip
|   |       |   |   |       qgeocodingmanager.sip
|   |       |   |   |       qgeocodingmanagerengine.sip
|   |       |   |   |       qgeomaneuver.sip
|   |       |   |   |       qgeoroute.sip
|   |       |   |   |       qgeoroutereply.sip
|   |       |   |   |       qgeorouterequest.sip
|   |       |   |   |       qgeoroutesegment.sip
|   |       |   |   |       qgeoroutingmanager.sip
|   |       |   |   |       qgeoroutingmanagerengine.sip
|   |       |   |   |       qgeoserviceprovider.sip
|   |       |   |   |       qlocation.sip
|   |       |   |   |       qplace.sip
|   |       |   |   |       qplaceattribute.sip
|   |       |   |   |       qplacecategory.sip
|   |       |   |   |       qplacecontactdetail.sip
|   |       |   |   |       qplacecontent.sip
|   |       |   |   |       qplacecontentreply.sip
|   |       |   |   |       qplacecontentrequest.sip
|   |       |   |   |       qplacedetailsreply.sip
|   |       |   |   |       qplaceeditorial.sip
|   |       |   |   |       qplaceicon.sip
|   |       |   |   |       qplaceidreply.sip
|   |       |   |   |       qplaceimage.sip
|   |       |   |   |       qplacemanager.sip
|   |       |   |   |       qplacemanagerengine.sip
|   |       |   |   |       qplacematchreply.sip
|   |       |   |   |       qplacematchrequest.sip
|   |       |   |   |       qplaceproposedsearchresult.sip
|   |       |   |   |       qplaceratings.sip
|   |       |   |   |       qplacereply.sip
|   |       |   |   |       qplaceresult.sip
|   |       |   |   |       qplacereview.sip
|   |       |   |   |       qplacesearchreply.sip
|   |       |   |   |       qplacesearchrequest.sip
|   |       |   |   |       qplacesearchresult.sip
|   |       |   |   |       qplacesearchsuggestionreply.sip
|   |       |   |   |       qplacesupplier.sip
|   |       |   |   |       qplaceuser.sip
|   |       |   |   |       QtLocation.toml
|   |       |   |   |       QtLocationmod.sip
|   |       |   |   |       
|   |       |   |   +---QtMultimedia
|   |       |   |   |       qabstractvideobuffer.sip
|   |       |   |   |       qabstractvideofilter.sip
|   |       |   |   |       qabstractvideosurface.sip
|   |       |   |   |       qaudio.sip
|   |       |   |   |       qaudiobuffer.sip
|   |       |   |   |       qaudiodecoder.sip
|   |       |   |   |       qaudiodecodercontrol.sip
|   |       |   |   |       qaudiodeviceinfo.sip
|   |       |   |   |       qaudioencodersettingscontrol.sip
|   |       |   |   |       qaudioformat.sip
|   |       |   |   |       qaudioinput.sip
|   |       |   |   |       qaudioinputselectorcontrol.sip
|   |       |   |   |       qaudiooutput.sip
|   |       |   |   |       qaudiooutputselectorcontrol.sip
|   |       |   |   |       qaudioprobe.sip
|   |       |   |   |       qaudiorecorder.sip
|   |       |   |   |       qaudiorolecontrol.sip
|   |       |   |   |       qcamera.sip
|   |       |   |   |       qcameracapturebufferformatcontrol.sip
|   |       |   |   |       qcameracapturedestinationcontrol.sip
|   |       |   |   |       qcameracontrol.sip
|   |       |   |   |       qcameraexposure.sip
|   |       |   |   |       qcameraexposurecontrol.sip
|   |       |   |   |       qcamerafeedbackcontrol.sip
|   |       |   |   |       qcameraflashcontrol.sip
|   |       |   |   |       qcamerafocus.sip
|   |       |   |   |       qcamerafocuscontrol.sip
|   |       |   |   |       qcameraimagecapture.sip
|   |       |   |   |       qcameraimagecapturecontrol.sip
|   |       |   |   |       qcameraimageprocessing.sip
|   |       |   |   |       qcameraimageprocessingcontrol.sip
|   |       |   |   |       qcamerainfo.sip
|   |       |   |   |       qcamerainfocontrol.sip
|   |       |   |   |       qcameralockscontrol.sip
|   |       |   |   |       qcameraviewfindersettings.sip
|   |       |   |   |       qcameraviewfindersettingscontrol.sip
|   |       |   |   |       qcamerazoomcontrol.sip
|   |       |   |   |       qcustomaudiorolecontrol.sip
|   |       |   |   |       qimageencodercontrol.sip
|   |       |   |   |       qmediaaudioprobecontrol.sip
|   |       |   |   |       qmediaavailabilitycontrol.sip
|   |       |   |   |       qmediabindableinterface.sip
|   |       |   |   |       qmediacontainercontrol.sip
|   |       |   |   |       qmediacontent.sip
|   |       |   |   |       qmediacontrol.sip
|   |       |   |   |       qmediaencodersettings.sip
|   |       |   |   |       qmediagaplessplaybackcontrol.sip
|   |       |   |   |       qmediametadata.sip
|   |       |   |   |       qmedianetworkaccesscontrol.sip
|   |       |   |   |       qmediaobject.sip
|   |       |   |   |       qmediaplayer.sip
|   |       |   |   |       qmediaplayercontrol.sip
|   |       |   |   |       qmediaplaylist.sip
|   |       |   |   |       qmediarecorder.sip
|   |       |   |   |       qmediarecordercontrol.sip
|   |       |   |   |       qmediaresource.sip
|   |       |   |   |       qmediaservice.sip
|   |       |   |   |       qmediastreamscontrol.sip
|   |       |   |   |       qmediatimerange.sip
|   |       |   |   |       qmediavideoprobecontrol.sip
|   |       |   |   |       qmetadatareadercontrol.sip
|   |       |   |   |       qmetadatawritercontrol.sip
|   |       |   |   |       qmultimedia.sip
|   |       |   |   |       qpymultimedia_qlist.sip
|   |       |   |   |       qradiodata.sip
|   |       |   |   |       qradiodatacontrol.sip
|   |       |   |   |       qradiotuner.sip
|   |       |   |   |       qradiotunercontrol.sip
|   |       |   |   |       qsound.sip
|   |       |   |   |       qsoundeffect.sip
|   |       |   |   |       QtMultimedia.toml
|   |       |   |   |       QtMultimediamod.sip
|   |       |   |   |       qvideodeviceselectorcontrol.sip
|   |       |   |   |       qvideoencodersettingscontrol.sip
|   |       |   |   |       qvideoframe.sip
|   |       |   |   |       qvideoprobe.sip
|   |       |   |   |       qvideorenderercontrol.sip
|   |       |   |   |       qvideosurfaceformat.sip
|   |       |   |   |       qvideowindowcontrol.sip
|   |       |   |   |       
|   |       |   |   +---QtMultimediaWidgets
|   |       |   |   |       qcameraviewfinder.sip
|   |       |   |   |       qgraphicsvideoitem.sip
|   |       |   |   |       QtMultimediaWidgets.toml
|   |       |   |   |       QtMultimediaWidgetsmod.sip
|   |       |   |   |       qvideowidget.sip
|   |       |   |   |       qvideowidgetcontrol.sip
|   |       |   |   |       
|   |       |   |   +---QtNetwork
|   |       |   |   |       qabstractnetworkcache.sip
|   |       |   |   |       qabstractsocket.sip
|   |       |   |   |       qauthenticator.sip
|   |       |   |   |       qdnslookup.sip
|   |       |   |   |       qhostaddress.sip
|   |       |   |   |       qhostinfo.sip
|   |       |   |   |       qhstspolicy.sip
|   |       |   |   |       qhttp2configuration.sip
|   |       |   |   |       qhttpmultipart.sip
|   |       |   |   |       qlocalserver.sip
|   |       |   |   |       qlocalsocket.sip
|   |       |   |   |       qnetworkaccessmanager.sip
|   |       |   |   |       qnetworkconfigmanager.sip
|   |       |   |   |       qnetworkconfiguration.sip
|   |       |   |   |       qnetworkcookie.sip
|   |       |   |   |       qnetworkcookiejar.sip
|   |       |   |   |       qnetworkdatagram.sip
|   |       |   |   |       qnetworkdiskcache.sip
|   |       |   |   |       qnetworkinterface.sip
|   |       |   |   |       qnetworkproxy.sip
|   |       |   |   |       qnetworkreply.sip
|   |       |   |   |       qnetworkrequest.sip
|   |       |   |   |       qnetworksession.sip
|   |       |   |   |       qocspresponse.sip
|   |       |   |   |       qpassworddigestor.sip
|   |       |   |   |       qpynetwork_qhash.sip
|   |       |   |   |       qpynetwork_qmap.sip
|   |       |   |   |       qssl.sip
|   |       |   |   |       qsslcertificate.sip
|   |       |   |   |       qsslcertificateextension.sip
|   |       |   |   |       qsslcipher.sip
|   |       |   |   |       qsslconfiguration.sip
|   |       |   |   |       qssldiffiehellmanparameters.sip
|   |       |   |   |       qsslellipticcurve.sip
|   |       |   |   |       qsslerror.sip
|   |       |   |   |       qsslkey.sip
|   |       |   |   |       qsslpresharedkeyauthenticator.sip
|   |       |   |   |       qsslsocket.sip
|   |       |   |   |       qtcpserver.sip
|   |       |   |   |       qtcpsocket.sip
|   |       |   |   |       QtNetwork.toml
|   |       |   |   |       QtNetworkmod.sip
|   |       |   |   |       qudpsocket.sip
|   |       |   |   |       
|   |       |   |   +---QtNfc
|   |       |   |   |       qndeffilter.sip
|   |       |   |   |       qndefmessage.sip
|   |       |   |   |       qndefnfcsmartposterrecord.sip
|   |       |   |   |       qndefnfctextrecord.sip
|   |       |   |   |       qndefnfcurirecord.sip
|   |       |   |   |       qndefrecord.sip
|   |       |   |   |       qnearfieldmanager.sip
|   |       |   |   |       qnearfieldsharemanager.sip
|   |       |   |   |       qnearfieldsharetarget.sip
|   |       |   |   |       qnearfieldtarget.sip
|   |       |   |   |       qqmlndefrecord.sip
|   |       |   |   |       QtNfc.toml
|   |       |   |   |       QtNfcmod.sip
|   |       |   |   |       
|   |       |   |   +---QtOpenGL
|   |       |   |   |       qgl.sip
|   |       |   |   |       QtOpenGL.toml
|   |       |   |   |       QtOpenGLmod.sip
|   |       |   |   |       
|   |       |   |   +---QtPositioning
|   |       |   |   |       qgeoaddress.sip
|   |       |   |   |       qgeoareamonitorinfo.sip
|   |       |   |   |       qgeoareamonitorsource.sip
|   |       |   |   |       qgeocircle.sip
|   |       |   |   |       qgeocoordinate.sip
|   |       |   |   |       qgeolocation.sip
|   |       |   |   |       qgeopath.sip
|   |       |   |   |       qgeopolygon.sip
|   |       |   |   |       qgeopositioninfo.sip
|   |       |   |   |       qgeopositioninfosource.sip
|   |       |   |   |       qgeorectangle.sip
|   |       |   |   |       qgeosatelliteinfo.sip
|   |       |   |   |       qgeosatelliteinfosource.sip
|   |       |   |   |       qgeoshape.sip
|   |       |   |   |       qnmeapositioninfosource.sip
|   |       |   |   |       QtPositioning.toml
|   |       |   |   |       QtPositioningmod.sip
|   |       |   |   |       
|   |       |   |   +---QtPrintSupport
|   |       |   |   |       qabstractprintdialog.sip
|   |       |   |   |       qpagesetupdialog.sip
|   |       |   |   |       qprintdialog.sip
|   |       |   |   |       qprintengine.sip
|   |       |   |   |       qprinter.sip
|   |       |   |   |       qprinterinfo.sip
|   |       |   |   |       qprintpreviewdialog.sip
|   |       |   |   |       qprintpreviewwidget.sip
|   |       |   |   |       qpyprintsupport_qlist.sip
|   |       |   |   |       QtPrintSupport.toml
|   |       |   |   |       QtPrintSupportmod.sip
|   |       |   |   |       
|   |       |   |   +---QtQml
|   |       |   |   |       qjsengine.sip
|   |       |   |   |       qjsvalue.sip
|   |       |   |   |       qjsvalueiterator.sip
|   |       |   |   |       qmlattachedpropertiesobject.sip
|   |       |   |   |       qmlregistertype.sip
|   |       |   |   |       qpyqmllistproperty.sip
|   |       |   |   |       qqml.sip
|   |       |   |   |       qqmlabstracturlinterceptor.sip
|   |       |   |   |       qqmlapplicationengine.sip
|   |       |   |   |       qqmlcomponent.sip
|   |       |   |   |       qqmlcontext.sip
|   |       |   |   |       qqmlengine.sip
|   |       |   |   |       qqmlerror.sip
|   |       |   |   |       qqmlexpression.sip
|   |       |   |   |       qqmlextensionplugin.sip
|   |       |   |   |       qqmlfileselector.sip
|   |       |   |   |       qqmlincubator.sip
|   |       |   |   |       qqmllist.sip
|   |       |   |   |       qqmlnetworkaccessmanagerfactory.sip
|   |       |   |   |       qqmlparserstatus.sip
|   |       |   |   |       qqmlproperty.sip
|   |       |   |   |       qqmlpropertymap.sip
|   |       |   |   |       qqmlpropertyvaluesource.sip
|   |       |   |   |       qqmlscriptstring.sip
|   |       |   |   |       QtQml.toml
|   |       |   |   |       QtQmlmod.sip
|   |       |   |   |       
|   |       |   |   +---QtQuick
|   |       |   |   |       qquickframebufferobject.sip
|   |       |   |   |       qquickimageprovider.sip
|   |       |   |   |       qquickitem.sip
|   |       |   |   |       qquickitemgrabresult.sip
|   |       |   |   |       qquickpainteditem.sip
|   |       |   |   |       qquickrendercontrol.sip
|   |       |   |   |       qquicktextdocument.sip
|   |       |   |   |       qquickview.sip
|   |       |   |   |       qquickwindow.sip
|   |       |   |   |       qsgabstractrenderer.sip
|   |       |   |   |       qsgengine.sip
|   |       |   |   |       qsgflatcolormaterial.sip
|   |       |   |   |       qsggeometry.sip
|   |       |   |   |       qsgimagenode.sip
|   |       |   |   |       qsgmaterial.sip
|   |       |   |   |       qsgmaterialrhishader.sip
|   |       |   |   |       qsgnode.sip
|   |       |   |   |       qsgrectanglenode.sip
|   |       |   |   |       qsgrendererinterface.sip
|   |       |   |   |       qsgrendernode.sip
|   |       |   |   |       qsgsimplerectnode.sip
|   |       |   |   |       qsgsimpletexturenode.sip
|   |       |   |   |       qsgtexture.sip
|   |       |   |   |       qsgtexturematerial.sip
|   |       |   |   |       qsgtextureprovider.sip
|   |       |   |   |       qsgvertexcolormaterial.sip
|   |       |   |   |       QtQuick.toml
|   |       |   |   |       QtQuickmod.sip
|   |       |   |   |       
|   |       |   |   +---QtQuick3D
|   |       |   |   |       qquick3d.sip
|   |       |   |   |       qquick3dgeometry.sip
|   |       |   |   |       qquick3dobject.sip
|   |       |   |   |       QtQuick3D.toml
|   |       |   |   |       QtQuick3Dmod.sip
|   |       |   |   |       
|   |       |   |   +---QtQuickWidgets
|   |       |   |   |       qquickwidget.sip
|   |       |   |   |       QtQuickWidgets.toml
|   |       |   |   |       QtQuickWidgetsmod.sip
|   |       |   |   |       
|   |       |   |   +---QtRemoteObjects
|   |       |   |   |       qremoteobjectabstractitemmodelreplica.sip
|   |       |   |   |       qremoteobjectdynamicreplica.sip
|   |       |   |   |       qremoteobjectnode.sip
|   |       |   |   |       qremoteobjectregistry.sip
|   |       |   |   |       qremoteobjectreplica.sip
|   |       |   |   |       qtremoteobjectglobal.sip
|   |       |   |   |       QtRemoteObjects.toml
|   |       |   |   |       QtRemoteObjectsmod.sip
|   |       |   |   |       
|   |       |   |   +---QtSensors
|   |       |   |   |       qaccelerometer.sip
|   |       |   |   |       qaltimeter.sip
|   |       |   |   |       qambientlightsensor.sip
|   |       |   |   |       qambienttemperaturesensor.sip
|   |       |   |   |       qcompass.sip
|   |       |   |   |       qdistancesensor.sip
|   |       |   |   |       qgyroscope.sip
|   |       |   |   |       qholstersensor.sip
|   |       |   |   |       qhumiditysensor.sip
|   |       |   |   |       qirproximitysensor.sip
|   |       |   |   |       qlidsensor.sip
|   |       |   |   |       qlightsensor.sip
|   |       |   |   |       qmagnetometer.sip
|   |       |   |   |       qorientationsensor.sip
|   |       |   |   |       qpressuresensor.sip
|   |       |   |   |       qproximitysensor.sip
|   |       |   |   |       qrotationsensor.sip
|   |       |   |   |       qsensor.sip
|   |       |   |   |       qtapsensor.sip
|   |       |   |   |       qtiltsensor.sip
|   |       |   |   |       QtSensors.toml
|   |       |   |   |       QtSensorsmod.sip
|   |       |   |   |       
|   |       |   |   +---QtSerialPort
|   |       |   |   |       qserialport.sip
|   |       |   |   |       qserialportinfo.sip
|   |       |   |   |       QtSerialPort.toml
|   |       |   |   |       QtSerialPortmod.sip
|   |       |   |   |       
|   |       |   |   +---QtSql
|   |       |   |   |       qsql.sip
|   |       |   |   |       qsqldatabase.sip
|   |       |   |   |       qsqldriver.sip
|   |       |   |   |       qsqlerror.sip
|   |       |   |   |       qsqlfield.sip
|   |       |   |   |       qsqlindex.sip
|   |       |   |   |       qsqlquery.sip
|   |       |   |   |       qsqlquerymodel.sip
|   |       |   |   |       qsqlrecord.sip
|   |       |   |   |       qsqlrelationaldelegate.sip
|   |       |   |   |       qsqlrelationaltablemodel.sip
|   |       |   |   |       qsqlresult.sip
|   |       |   |   |       qsqltablemodel.sip
|   |       |   |   |       QtSql.toml
|   |       |   |   |       qtsqlglobal.sip
|   |       |   |   |       QtSqlmod.sip
|   |       |   |   |       
|   |       |   |   +---QtSvg
|   |       |   |   |       qgraphicssvgitem.sip
|   |       |   |   |       qsvggenerator.sip
|   |       |   |   |       qsvgrenderer.sip
|   |       |   |   |       qsvgwidget.sip
|   |       |   |   |       QtSvg.toml
|   |       |   |   |       QtSvgmod.sip
|   |       |   |   |       
|   |       |   |   +---QtTest
|   |       |   |   |       qabstractitemmodeltester.sip
|   |       |   |   |       qsignalspy.sip
|   |       |   |   |       qtestcase.sip
|   |       |   |   |       qtestkeyboard.sip
|   |       |   |   |       qtestmouse.sip
|   |       |   |   |       qtestsystem.sip
|   |       |   |   |       qtesttouch.sip
|   |       |   |   |       QtTest.toml
|   |       |   |   |       QtTestmod.sip
|   |       |   |   |       
|   |       |   |   +---QtTextToSpeech
|   |       |   |   |       qtexttospeech.sip
|   |       |   |   |       QtTextToSpeech.toml
|   |       |   |   |       QtTextToSpeechmod.sip
|   |       |   |   |       qvoice.sip
|   |       |   |   |       
|   |       |   |   +---QtWebChannel
|   |       |   |   |       QtWebChannel.toml
|   |       |   |   |       QtWebChannelmod.sip
|   |       |   |   |       qwebchannel.sip
|   |       |   |   |       qwebchannelabstracttransport.sip
|   |       |   |   |       
|   |       |   |   +---QtWebSockets
|   |       |   |   |       qmaskgenerator.sip
|   |       |   |   |       QtWebSockets.toml
|   |       |   |   |       QtWebSocketsmod.sip
|   |       |   |   |       qwebsocket.sip
|   |       |   |   |       qwebsocketcorsauthenticator.sip
|   |       |   |   |       qwebsocketprotocol.sip
|   |       |   |   |       qwebsocketserver.sip
|   |       |   |   |       
|   |       |   |   +---QtWidgets
|   |       |   |   |       qabstractbutton.sip
|   |       |   |   |       qabstractitemdelegate.sip
|   |       |   |   |       qabstractitemview.sip
|   |       |   |   |       qabstractscrollarea.sip
|   |       |   |   |       qabstractslider.sip
|   |       |   |   |       qabstractspinbox.sip
|   |       |   |   |       qaction.sip
|   |       |   |   |       qactiongroup.sip
|   |       |   |   |       qapplication.sip
|   |       |   |   |       qboxlayout.sip
|   |       |   |   |       qbuttongroup.sip
|   |       |   |   |       qcalendarwidget.sip
|   |       |   |   |       qcheckbox.sip
|   |       |   |   |       qcolordialog.sip
|   |       |   |   |       qcolumnview.sip
|   |       |   |   |       qcombobox.sip
|   |       |   |   |       qcommandlinkbutton.sip
|   |       |   |   |       qcommonstyle.sip
|   |       |   |   |       qcompleter.sip
|   |       |   |   |       qdatawidgetmapper.sip
|   |       |   |   |       qdatetimeedit.sip
|   |       |   |   |       qdesktopwidget.sip
|   |       |   |   |       qdial.sip
|   |       |   |   |       qdialog.sip
|   |       |   |   |       qdialogbuttonbox.sip
|   |       |   |   |       qdirmodel.sip
|   |       |   |   |       qdockwidget.sip
|   |       |   |   |       qdrawutil.sip
|   |       |   |   |       qerrormessage.sip
|   |       |   |   |       qfiledialog.sip
|   |       |   |   |       qfileiconprovider.sip
|   |       |   |   |       qfilesystemmodel.sip
|   |       |   |   |       qfocusframe.sip
|   |       |   |   |       qfontcombobox.sip
|   |       |   |   |       qfontdialog.sip
|   |       |   |   |       qformlayout.sip
|   |       |   |   |       qframe.sip
|   |       |   |   |       qgesture.sip
|   |       |   |   |       qgesturerecognizer.sip
|   |       |   |   |       qgraphicsanchorlayout.sip
|   |       |   |   |       qgraphicseffect.sip
|   |       |   |   |       qgraphicsgridlayout.sip
|   |       |   |   |       qgraphicsitem.sip
|   |       |   |   |       qgraphicslayout.sip
|   |       |   |   |       qgraphicslayoutitem.sip
|   |       |   |   |       qgraphicslinearlayout.sip
|   |       |   |   |       qgraphicsproxywidget.sip
|   |       |   |   |       qgraphicsscene.sip
|   |       |   |   |       qgraphicssceneevent.sip
|   |       |   |   |       qgraphicstransform.sip
|   |       |   |   |       qgraphicsview.sip
|   |       |   |   |       qgraphicswidget.sip
|   |       |   |   |       qgridlayout.sip
|   |       |   |   |       qgroupbox.sip
|   |       |   |   |       qheaderview.sip
|   |       |   |   |       qinputdialog.sip
|   |       |   |   |       qitemdelegate.sip
|   |       |   |   |       qitemeditorfactory.sip
|   |       |   |   |       qkeyeventtransition.sip
|   |       |   |   |       qkeysequenceedit.sip
|   |       |   |   |       qlabel.sip
|   |       |   |   |       qlayout.sip
|   |       |   |   |       qlayoutitem.sip
|   |       |   |   |       qlcdnumber.sip
|   |       |   |   |       qlineedit.sip
|   |       |   |   |       qlistview.sip
|   |       |   |   |       qlistwidget.sip
|   |       |   |   |       qmaccocoaviewcontainer.sip
|   |       |   |   |       qmainwindow.sip
|   |       |   |   |       qmdiarea.sip
|   |       |   |   |       qmdisubwindow.sip
|   |       |   |   |       qmenu.sip
|   |       |   |   |       qmenubar.sip
|   |       |   |   |       qmessagebox.sip
|   |       |   |   |       qmouseeventtransition.sip
|   |       |   |   |       qopenglwidget.sip
|   |       |   |   |       qplaintextedit.sip
|   |       |   |   |       qprogressbar.sip
|   |       |   |   |       qprogressdialog.sip
|   |       |   |   |       qproxystyle.sip
|   |       |   |   |       qpushbutton.sip
|   |       |   |   |       qpywidgets_qlist.sip
|   |       |   |   |       qradiobutton.sip
|   |       |   |   |       qrubberband.sip
|   |       |   |   |       qscrollarea.sip
|   |       |   |   |       qscrollbar.sip
|   |       |   |   |       qscroller.sip
|   |       |   |   |       qscrollerproperties.sip
|   |       |   |   |       qshortcut.sip
|   |       |   |   |       qsizegrip.sip
|   |       |   |   |       qsizepolicy.sip
|   |       |   |   |       qslider.sip
|   |       |   |   |       qspinbox.sip
|   |       |   |   |       qsplashscreen.sip
|   |       |   |   |       qsplitter.sip
|   |       |   |   |       qstackedlayout.sip
|   |       |   |   |       qstackedwidget.sip
|   |       |   |   |       qstatusbar.sip
|   |       |   |   |       qstyle.sip
|   |       |   |   |       qstyleditemdelegate.sip
|   |       |   |   |       qstylefactory.sip
|   |       |   |   |       qstyleoption.sip
|   |       |   |   |       qstylepainter.sip
|   |       |   |   |       qsystemtrayicon.sip
|   |       |   |   |       qtabbar.sip
|   |       |   |   |       qtableview.sip
|   |       |   |   |       qtablewidget.sip
|   |       |   |   |       qtabwidget.sip
|   |       |   |   |       qtextbrowser.sip
|   |       |   |   |       qtextedit.sip
|   |       |   |   |       qtoolbar.sip
|   |       |   |   |       qtoolbox.sip
|   |       |   |   |       qtoolbutton.sip
|   |       |   |   |       qtooltip.sip
|   |       |   |   |       qtreeview.sip
|   |       |   |   |       qtreewidget.sip
|   |       |   |   |       qtreewidgetitemiterator.sip
|   |       |   |   |       QtWidgets.toml
|   |       |   |   |       QtWidgetsmod.sip
|   |       |   |   |       qundogroup.sip
|   |       |   |   |       qundostack.sip
|   |       |   |   |       qundoview.sip
|   |       |   |   |       qwhatsthis.sip
|   |       |   |   |       qwidget.sip
|   |       |   |   |       qwidgetaction.sip
|   |       |   |   |       qwizard.sip
|   |       |   |   |       
|   |       |   |   +---QtWinExtras
|   |       |   |   |       QtWinExtras.toml
|   |       |   |   |       QtWinExtrasmod.sip
|   |       |   |   |       qwinfunctions.sip
|   |       |   |   |       qwinjumplist.sip
|   |       |   |   |       qwinjumplistcategory.sip
|   |       |   |   |       qwinjumplistitem.sip
|   |       |   |   |       qwintaskbarbutton.sip
|   |       |   |   |       qwintaskbarprogress.sip
|   |       |   |   |       qwinthumbnailtoolbar.sip
|   |       |   |   |       qwinthumbnailtoolbutton.sip
|   |       |   |   |       
|   |       |   |   +---QtXml
|   |       |   |   |       qdom.sip
|   |       |   |   |       QtXml.toml
|   |       |   |   |       QtXmlmod.sip
|   |       |   |   |       qxml.sip
|   |       |   |   |       
|   |       |   |   \---QtXmlPatterns
|   |       |   |           qabstractmessagehandler.sip
|   |       |   |           qabstracturiresolver.sip
|   |       |   |           qabstractxmlnodemodel.sip
|   |       |   |           qabstractxmlreceiver.sip
|   |       |   |           qsimplexmlnodemodel.sip
|   |       |   |           qsourcelocation.sip
|   |       |   |           QtXmlPatterns.toml
|   |       |   |           QtXmlPatternsmod.sip
|   |       |   |           qxmlformatter.sip
|   |       |   |           qxmlname.sip
|   |       |   |           qxmlnamepool.sip
|   |       |   |           qxmlquery.sip
|   |       |   |           qxmlresultitems.sip
|   |       |   |           qxmlschema.sip
|   |       |   |           qxmlschemavalidator.sip
|   |       |   |           qxmlserializer.sip
|   |       |   |           
|   |       |   +---Qt5
|   |       |   |   +---bin
|   |       |   |   |       concrt140.dll
|   |       |   |   |       d3dcompiler_47.dll
|   |       |   |   |       libcrypto-1_1-x64.dll
|   |       |   |   |       libeay32.dll
|   |       |   |   |       libEGL.dll
|   |       |   |   |       libGLESv2.dll
|   |       |   |   |       libssl-1_1-x64.dll
|   |       |   |   |       msvcp140.dll
|   |       |   |   |       msvcp140_1.dll
|   |       |   |   |       msvcp140_2.dll
|   |       |   |   |       opengl32sw.dll
|   |       |   |   |       Qt5Bluetooth.dll
|   |       |   |   |       Qt5Core.dll
|   |       |   |   |       Qt5DBus.dll
|   |       |   |   |       Qt5Designer.dll
|   |       |   |   |       Qt5Gui.dll
|   |       |   |   |       Qt5Help.dll
|   |       |   |   |       Qt5Location.dll
|   |       |   |   |       Qt5Multimedia.dll
|   |       |   |   |       Qt5MultimediaWidgets.dll
|   |       |   |   |       Qt5Network.dll
|   |       |   |   |       Qt5Nfc.dll
|   |       |   |   |       Qt5OpenGL.dll
|   |       |   |   |       Qt5Positioning.dll
|   |       |   |   |       Qt5PositioningQuick.dll
|   |       |   |   |       Qt5PrintSupport.dll
|   |       |   |   |       Qt5Qml.dll
|   |       |   |   |       Qt5QmlModels.dll
|   |       |   |   |       Qt5QmlWorkerScript.dll
|   |       |   |   |       Qt5Quick.dll
|   |       |   |   |       Qt5Quick3D.dll
|   |       |   |   |       Qt5Quick3DAssetImport.dll
|   |       |   |   |       Qt5Quick3DRender.dll
|   |       |   |   |       Qt5Quick3DRuntimeRender.dll
|   |       |   |   |       Qt5Quick3DUtils.dll
|   |       |   |   |       Qt5QuickControls2.dll
|   |       |   |   |       Qt5QuickParticles.dll
|   |       |   |   |       Qt5QuickShapes.dll
|   |       |   |   |       Qt5QuickTemplates2.dll
|   |       |   |   |       Qt5QuickTest.dll
|   |       |   |   |       Qt5QuickWidgets.dll
|   |       |   |   |       Qt5RemoteObjects.dll
|   |       |   |   |       Qt5Sensors.dll
|   |       |   |   |       Qt5SerialPort.dll
|   |       |   |   |       Qt5Sql.dll
|   |       |   |   |       Qt5Svg.dll
|   |       |   |   |       Qt5Test.dll
|   |       |   |   |       Qt5TextToSpeech.dll
|   |       |   |   |       Qt5WebChannel.dll
|   |       |   |   |       Qt5WebSockets.dll
|   |       |   |   |       Qt5WebView.dll
|   |       |   |   |       Qt5Widgets.dll
|   |       |   |   |       Qt5WinExtras.dll
|   |       |   |   |       Qt5Xml.dll
|   |       |   |   |       Qt5XmlPatterns.dll
|   |       |   |   |       ssleay32.dll
|   |       |   |   |       vcruntime140.dll
|   |       |   |   |       vcruntime140_1.dll
|   |       |   |   |       
|   |       |   |   +---plugins
|   |       |   |   |   +---assetimporters
|   |       |   |   |   |       assimp.dll
|   |       |   |   |   |       uip.dll
|   |       |   |   |   |       
|   |       |   |   |   +---audio
|   |       |   |   |   |       qtaudio_wasapi.dll
|   |       |   |   |   |       qtaudio_windows.dll
|   |       |   |   |   |       
|   |       |   |   |   +---bearer
|   |       |   |   |   |       qgenericbearer.dll
|   |       |   |   |   |       
|   |       |   |   |   +---generic
|   |       |   |   |   |       qtuiotouchplugin.dll
|   |       |   |   |   |       
|   |       |   |   |   +---geometryloaders
|   |       |   |   |   |       defaultgeometryloader.dll
|   |       |   |   |   |       gltfgeometryloader.dll
|   |       |   |   |   |       
|   |       |   |   |   +---geoservices
|   |       |   |   |   |       qtgeoservices_esri.dll
|   |       |   |   |   |       qtgeoservices_itemsoverlay.dll
|   |       |   |   |   |       qtgeoservices_mapbox.dll
|   |       |   |   |   |       qtgeoservices_nokia.dll
|   |       |   |   |   |       qtgeoservices_osm.dll
|   |       |   |   |   |       
|   |       |   |   |   +---iconengines
|   |       |   |   |   |       qsvgicon.dll
|   |       |   |   |   |       
|   |       |   |   |   +---imageformats
|   |       |   |   |   |       qgif.dll
|   |       |   |   |   |       qicns.dll
|   |       |   |   |   |       qico.dll
|   |       |   |   |   |       qjpeg.dll
|   |       |   |   |   |       qsvg.dll
|   |       |   |   |   |       qtga.dll
|   |       |   |   |   |       qtiff.dll
|   |       |   |   |   |       qwbmp.dll
|   |       |   |   |   |       qwebp.dll
|   |       |   |   |   |       
|   |       |   |   |   +---mediaservice
|   |       |   |   |   |       dsengine.dll
|   |       |   |   |   |       qtmedia_audioengine.dll
|   |       |   |   |   |       wmfengine.dll
|   |       |   |   |   |       
|   |       |   |   |   +---platforms
|   |       |   |   |   |       qminimal.dll
|   |       |   |   |   |       qoffscreen.dll
|   |       |   |   |   |       qwebgl.dll
|   |       |   |   |   |       qwindows.dll
|   |       |   |   |   |       
|   |       |   |   |   +---platformthemes
|   |       |   |   |   |       qxdgdesktopportal.dll
|   |       |   |   |   |       
|   |       |   |   |   +---playlistformats
|   |       |   |   |   |       qtmultimedia_m3u.dll
|   |       |   |   |   |       
|   |       |   |   |   +---position
|   |       |   |   |   |       qtposition_positionpoll.dll
|   |       |   |   |   |       qtposition_serialnmea.dll
|   |       |   |   |   |       qtposition_winrt.dll
|   |       |   |   |   |       
|   |       |   |   |   +---printsupport
|   |       |   |   |   |       windowsprintersupport.dll
|   |       |   |   |   |       
|   |       |   |   |   +---renderers
|   |       |   |   |   |       openglrenderer.dll
|   |       |   |   |   |       
|   |       |   |   |   +---sceneparsers
|   |       |   |   |   |       gltfsceneexport.dll
|   |       |   |   |   |       gltfsceneimport.dll
|   |       |   |   |   |       
|   |       |   |   |   +---sensorgestures
|   |       |   |   |   |       qtsensorgestures_plugin.dll
|   |       |   |   |   |       qtsensorgestures_shakeplugin.dll
|   |       |   |   |   |       
|   |       |   |   |   +---sensors
|   |       |   |   |   |       qtsensors_generic.dll
|   |       |   |   |   |       
|   |       |   |   |   +---sqldrivers
|   |       |   |   |   |       qsqlite.dll
|   |       |   |   |   |       qsqlodbc.dll
|   |       |   |   |   |       qsqlpsql.dll
|   |       |   |   |   |       
|   |       |   |   |   +---styles
|   |       |   |   |   |       qwindowsvistastyle.dll
|   |       |   |   |   |       
|   |       |   |   |   +---texttospeech
|   |       |   |   |   |       qtexttospeech_sapi.dll
|   |       |   |   |   |       
|   |       |   |   |   \---webview
|   |       |   |   |           qtwebview_webengine.dll
|   |       |   |   |           
|   |       |   |   +---qml
|   |       |   |   |   +---Qt
|   |       |   |   |   |   +---labs
|   |       |   |   |   |   |   +---animation
|   |       |   |   |   |   |   |       labsanimationplugin.dll
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---calendar
|   |       |   |   |   |   |   |       DayOfWeekRow.qml
|   |       |   |   |   |   |   |       DayOfWeekRow.qmlc
|   |       |   |   |   |   |   |       MonthGrid.qml
|   |       |   |   |   |   |   |       MonthGrid.qmlc
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qtlabscalendarplugin.dll
|   |       |   |   |   |   |   |       WeekNumberColumn.qml
|   |       |   |   |   |   |   |       WeekNumberColumn.qmlc
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---folderlistmodel
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qmlfolderlistmodelplugin.dll
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---location
|   |       |   |   |   |   |   |       locationlabsplugin.dll
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---platform
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qtlabsplatformplugin.dll
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---qmlmodels
|   |       |   |   |   |   |   |       labsmodelsplugin.dll
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---settings
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qmlsettingsplugin.dll
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---sharedimage
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       sharedimageplugin.dll
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   \---wavefrontmesh
|   |       |   |   |   |   |           plugins.qmltypes
|   |       |   |   |   |   |           qmldir
|   |       |   |   |   |   |           qmlwavefrontmeshplugin.dll
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---test
|   |       |   |   |   |   |   \---qtestroot
|   |       |   |   |   |   |           plugins.qmltypes
|   |       |   |   |   |   |           qmldir
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---WebSockets
|   |       |   |   |   |           qmldir
|   |       |   |   |   |           
|   |       |   |   |   +---QtBluetooth
|   |       |   |   |   |       declarative_bluetooth.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   +---QtGraphicalEffects
|   |       |   |   |   |   |   Blend.qml
|   |       |   |   |   |   |   BrightnessContrast.qml
|   |       |   |   |   |   |   Colorize.qml
|   |       |   |   |   |   |   ColorOverlay.qml
|   |       |   |   |   |   |   ConicalGradient.qml
|   |       |   |   |   |   |   Desaturate.qml
|   |       |   |   |   |   |   DirectionalBlur.qml
|   |       |   |   |   |   |   Displace.qml
|   |       |   |   |   |   |   DropShadow.qml
|   |       |   |   |   |   |   FastBlur.qml
|   |       |   |   |   |   |   GammaAdjust.qml
|   |       |   |   |   |   |   GaussianBlur.qml
|   |       |   |   |   |   |   Glow.qml
|   |       |   |   |   |   |   HueSaturation.qml
|   |       |   |   |   |   |   InnerShadow.qml
|   |       |   |   |   |   |   LevelAdjust.qml
|   |       |   |   |   |   |   LinearGradient.qml
|   |       |   |   |   |   |   MaskedBlur.qml
|   |       |   |   |   |   |   OpacityMask.qml
|   |       |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   qmldir
|   |       |   |   |   |   |   qtgraphicaleffectsplugin.dll
|   |       |   |   |   |   |   RadialBlur.qml
|   |       |   |   |   |   |   RadialGradient.qml
|   |       |   |   |   |   |   RectangularGlow.qml
|   |       |   |   |   |   |   RecursiveBlur.qml
|   |       |   |   |   |   |   ThresholdMask.qml
|   |       |   |   |   |   |   ZoomBlur.qml
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---private
|   |       |   |   |   |           DropShadowBase.qml
|   |       |   |   |   |           DropShadowBase.qmlc
|   |       |   |   |   |           FastGlow.qml
|   |       |   |   |   |           FastGlow.qmlc
|   |       |   |   |   |           FastInnerShadow.qml
|   |       |   |   |   |           FastInnerShadow.qmlc
|   |       |   |   |   |           FastMaskedBlur.qml
|   |       |   |   |   |           FastMaskedBlur.qmlc
|   |       |   |   |   |           GaussianDirectionalBlur.qml
|   |       |   |   |   |           GaussianDirectionalBlur.qmlc
|   |       |   |   |   |           GaussianGlow.qml
|   |       |   |   |   |           GaussianGlow.qmlc
|   |       |   |   |   |           GaussianInnerShadow.qml
|   |       |   |   |   |           GaussianInnerShadow.qmlc
|   |       |   |   |   |           GaussianMaskedBlur.qml
|   |       |   |   |   |           GaussianMaskedBlur.qmlc
|   |       |   |   |   |           qmldir
|   |       |   |   |   |           qtgraphicaleffectsprivate.dll
|   |       |   |   |   |           
|   |       |   |   |   +---QtLocation
|   |       |   |   |   |       declarative_location.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   +---QtMultimedia
|   |       |   |   |   |       declarative_multimedia.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       Video.qml
|   |       |   |   |   |       
|   |       |   |   |   +---QtNfc
|   |       |   |   |   |       declarative_nfc.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   +---QtPositioning
|   |       |   |   |   |       declarative_positioning.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   +---QtQml
|   |       |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   qmldir
|   |       |   |   |   |   |   qmlplugin.dll
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---Models.2
|   |       |   |   |   |   |       modelsplugin.dll
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---RemoteObjects
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qtqmlremoteobjects.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---StateMachine
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qtqmlstatemachine.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   \---WorkerScript.2
|   |       |   |   |   |           plugins.qmltypes
|   |       |   |   |   |           qmldir
|   |       |   |   |   |           workerscriptplugin.dll
|   |       |   |   |   |           
|   |       |   |   |   +---QtQuick
|   |       |   |   |   |   +---Controls
|   |       |   |   |   |   |   |   ApplicationWindow.qml
|   |       |   |   |   |   |   |   ApplicationWindow.qmlc
|   |       |   |   |   |   |   |   BusyIndicator.qml
|   |       |   |   |   |   |   |   BusyIndicator.qmlc
|   |       |   |   |   |   |   |   Button.qml
|   |       |   |   |   |   |   |   Button.qmlc
|   |       |   |   |   |   |   |   Calendar.qml
|   |       |   |   |   |   |   |   Calendar.qmlc
|   |       |   |   |   |   |   |   CheckBox.qml
|   |       |   |   |   |   |   |   CheckBox.qmlc
|   |       |   |   |   |   |   |   ComboBox.qml
|   |       |   |   |   |   |   |   ComboBox.qmlc
|   |       |   |   |   |   |   |   GroupBox.qml
|   |       |   |   |   |   |   |   GroupBox.qmlc
|   |       |   |   |   |   |   |   Label.qml
|   |       |   |   |   |   |   |   Label.qmlc
|   |       |   |   |   |   |   |   Menu.qml
|   |       |   |   |   |   |   |   Menu.qmlc
|   |       |   |   |   |   |   |   MenuBar.qml
|   |       |   |   |   |   |   |   MenuBar.qmlc
|   |       |   |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   |   ProgressBar.qml
|   |       |   |   |   |   |   |   ProgressBar.qmlc
|   |       |   |   |   |   |   |   qmldir
|   |       |   |   |   |   |   |   qtquickcontrolsplugin.dll
|   |       |   |   |   |   |   |   RadioButton.qml
|   |       |   |   |   |   |   |   RadioButton.qmlc
|   |       |   |   |   |   |   |   ScrollView.qml
|   |       |   |   |   |   |   |   ScrollView.qmlc
|   |       |   |   |   |   |   |   Slider.qml
|   |       |   |   |   |   |   |   Slider.qmlc
|   |       |   |   |   |   |   |   SpinBox.qml
|   |       |   |   |   |   |   |   SpinBox.qmlc
|   |       |   |   |   |   |   |   SplitView.qml
|   |       |   |   |   |   |   |   SplitView.qmlc
|   |       |   |   |   |   |   |   StackView.qml
|   |       |   |   |   |   |   |   StackView.qmlc
|   |       |   |   |   |   |   |   StackViewDelegate.qml
|   |       |   |   |   |   |   |   StackViewDelegate.qmlc
|   |       |   |   |   |   |   |   StackViewTransition.qml
|   |       |   |   |   |   |   |   StackViewTransition.qmlc
|   |       |   |   |   |   |   |   StatusBar.qml
|   |       |   |   |   |   |   |   StatusBar.qmlc
|   |       |   |   |   |   |   |   Switch.qml
|   |       |   |   |   |   |   |   Switch.qmlc
|   |       |   |   |   |   |   |   Tab.qml
|   |       |   |   |   |   |   |   Tab.qmlc
|   |       |   |   |   |   |   |   TableView.qml
|   |       |   |   |   |   |   |   TableView.qmlc
|   |       |   |   |   |   |   |   TableViewColumn.qml
|   |       |   |   |   |   |   |   TableViewColumn.qmlc
|   |       |   |   |   |   |   |   TabView.qml
|   |       |   |   |   |   |   |   TabView.qmlc
|   |       |   |   |   |   |   |   TextArea.qml
|   |       |   |   |   |   |   |   TextArea.qmlc
|   |       |   |   |   |   |   |   TextField.qml
|   |       |   |   |   |   |   |   TextField.qmlc
|   |       |   |   |   |   |   |   ToolBar.qml
|   |       |   |   |   |   |   |   ToolBar.qmlc
|   |       |   |   |   |   |   |   ToolButton.qml
|   |       |   |   |   |   |   |   ToolButton.qmlc
|   |       |   |   |   |   |   |   TreeView.qml
|   |       |   |   |   |   |   |   TreeView.qmlc
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---Private
|   |       |   |   |   |   |   |       AbstractCheckable.qml
|   |       |   |   |   |   |   |       AbstractCheckable.qmlc
|   |       |   |   |   |   |   |       BasicButton.qml
|   |       |   |   |   |   |   |       BasicButton.qmlc
|   |       |   |   |   |   |   |       BasicTableView.qml
|   |       |   |   |   |   |   |       BasicTableView.qmlc
|   |       |   |   |   |   |   |       CalendarHeaderModel.qml
|   |       |   |   |   |   |   |       CalendarHeaderModel.qmlc
|   |       |   |   |   |   |   |       CalendarUtils.js
|   |       |   |   |   |   |   |       CalendarUtils.jsc
|   |       |   |   |   |   |   |       ColumnMenuContent.qml
|   |       |   |   |   |   |   |       ColumnMenuContent.qmlc
|   |       |   |   |   |   |   |       ContentItem.qml
|   |       |   |   |   |   |   |       ContentItem.qmlc
|   |       |   |   |   |   |   |       Control.qml
|   |       |   |   |   |   |   |       Control.qmlc
|   |       |   |   |   |   |   |       EditMenu.qml
|   |       |   |   |   |   |   |       EditMenu.qmlc
|   |       |   |   |   |   |   |       EditMenu_base.qml
|   |       |   |   |   |   |   |       EditMenu_base.qmlc
|   |       |   |   |   |   |   |       FastGlow.qml
|   |       |   |   |   |   |   |       FastGlow.qmlc
|   |       |   |   |   |   |   |       FocusFrame.qml
|   |       |   |   |   |   |   |       FocusFrame.qmlc
|   |       |   |   |   |   |   |       HoverButton.qml
|   |       |   |   |   |   |   |       HoverButton.qmlc
|   |       |   |   |   |   |   |       MenuContentItem.qml
|   |       |   |   |   |   |   |       MenuContentItem.qmlc
|   |       |   |   |   |   |   |       MenuContentScroller.qml
|   |       |   |   |   |   |   |       MenuContentScroller.qmlc
|   |       |   |   |   |   |   |       MenuItemSubControls.qml
|   |       |   |   |   |   |   |       MenuItemSubControls.qmlc
|   |       |   |   |   |   |   |       ModalPopupBehavior.qml
|   |       |   |   |   |   |   |       ModalPopupBehavior.qmlc
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       ScrollBar.qml
|   |       |   |   |   |   |   |       ScrollBar.qmlc
|   |       |   |   |   |   |   |       ScrollViewHelper.qml
|   |       |   |   |   |   |   |       ScrollViewHelper.qmlc
|   |       |   |   |   |   |   |       SourceProxy.qml
|   |       |   |   |   |   |   |       SourceProxy.qmlc
|   |       |   |   |   |   |   |       StackView.js
|   |       |   |   |   |   |   |       StackView.jsc
|   |       |   |   |   |   |   |       StackViewSlideDelegate.qml
|   |       |   |   |   |   |   |       StackViewSlideDelegate.qmlc
|   |       |   |   |   |   |   |       style.js
|   |       |   |   |   |   |   |       style.jsc
|   |       |   |   |   |   |   |       Style.qml
|   |       |   |   |   |   |   |       Style.qmlc
|   |       |   |   |   |   |   |       SystemPaletteSingleton.qml
|   |       |   |   |   |   |   |       SystemPaletteSingleton.qmlc
|   |       |   |   |   |   |   |       TabBar.qml
|   |       |   |   |   |   |   |       TabBar.qmlc
|   |       |   |   |   |   |   |       TableViewItemDelegateLoader.qml
|   |       |   |   |   |   |   |       TableViewItemDelegateLoader.qmlc
|   |       |   |   |   |   |   |       TableViewSelection.qml
|   |       |   |   |   |   |   |       TableViewSelection.qmlc
|   |       |   |   |   |   |   |       TextHandle.qml
|   |       |   |   |   |   |   |       TextHandle.qmlc
|   |       |   |   |   |   |   |       TextInputWithHandles.qml
|   |       |   |   |   |   |   |       TextInputWithHandles.qmlc
|   |       |   |   |   |   |   |       TextSingleton.qml
|   |       |   |   |   |   |   |       TextSingleton.qmlc
|   |       |   |   |   |   |   |       ToolMenuButton.qml
|   |       |   |   |   |   |   |       ToolMenuButton.qmlc
|   |       |   |   |   |   |   |       TreeViewItemDelegateLoader.qml
|   |       |   |   |   |   |   |       TreeViewItemDelegateLoader.qmlc
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   \---Styles
|   |       |   |   |   |   |       |   qmldir
|   |       |   |   |   |   |       |   
|   |       |   |   |   |   |       +---Base
|   |       |   |   |   |   |       |   |   ApplicationWindowStyle.qml
|   |       |   |   |   |   |       |   |   ApplicationWindowStyle.qmlc
|   |       |   |   |   |   |       |   |   BasicTableViewStyle.qml
|   |       |   |   |   |   |       |   |   BasicTableViewStyle.qmlc
|   |       |   |   |   |   |       |   |   BusyIndicatorStyle.qml
|   |       |   |   |   |   |       |   |   BusyIndicatorStyle.qmlc
|   |       |   |   |   |   |       |   |   ButtonStyle.qml
|   |       |   |   |   |   |       |   |   ButtonStyle.qmlc
|   |       |   |   |   |   |       |   |   CalendarStyle.qml
|   |       |   |   |   |   |       |   |   CalendarStyle.qmlc
|   |       |   |   |   |   |       |   |   CheckBoxStyle.qml
|   |       |   |   |   |   |       |   |   CheckBoxStyle.qmlc
|   |       |   |   |   |   |       |   |   CircularButtonStyle.qml
|   |       |   |   |   |   |       |   |   CircularButtonStyle.qmlc
|   |       |   |   |   |   |       |   |   CircularGaugeStyle.qml
|   |       |   |   |   |   |       |   |   CircularGaugeStyle.qmlc
|   |       |   |   |   |   |       |   |   CircularTickmarkLabelStyle.qml
|   |       |   |   |   |   |       |   |   CircularTickmarkLabelStyle.qmlc
|   |       |   |   |   |   |       |   |   ComboBoxStyle.qml
|   |       |   |   |   |   |       |   |   ComboBoxStyle.qmlc
|   |       |   |   |   |   |       |   |   CommonStyleHelper.qml
|   |       |   |   |   |   |       |   |   CommonStyleHelper.qmlc
|   |       |   |   |   |   |       |   |   DelayButtonStyle.qml
|   |       |   |   |   |   |       |   |   DelayButtonStyle.qmlc
|   |       |   |   |   |   |       |   |   DialStyle.qml
|   |       |   |   |   |   |       |   |   DialStyle.qmlc
|   |       |   |   |   |   |       |   |   FocusFrameStyle.qml
|   |       |   |   |   |   |       |   |   FocusFrameStyle.qmlc
|   |       |   |   |   |   |       |   |   GaugeStyle.qml
|   |       |   |   |   |   |       |   |   GaugeStyle.qmlc
|   |       |   |   |   |   |       |   |   GroupBoxStyle.qml
|   |       |   |   |   |   |       |   |   GroupBoxStyle.qmlc
|   |       |   |   |   |   |       |   |   HandleStyle.qml
|   |       |   |   |   |   |       |   |   HandleStyle.qmlc
|   |       |   |   |   |   |       |   |   HandleStyleHelper.qml
|   |       |   |   |   |   |       |   |   HandleStyleHelper.qmlc
|   |       |   |   |   |   |       |   |   MenuBarStyle.qml
|   |       |   |   |   |   |       |   |   MenuBarStyle.qmlc
|   |       |   |   |   |   |       |   |   MenuStyle.qml
|   |       |   |   |   |   |       |   |   MenuStyle.qmlc
|   |       |   |   |   |   |       |   |   PieMenuStyle.qml
|   |       |   |   |   |   |       |   |   PieMenuStyle.qmlc
|   |       |   |   |   |   |       |   |   ProgressBarStyle.qml
|   |       |   |   |   |   |       |   |   ProgressBarStyle.qmlc
|   |       |   |   |   |   |       |   |   RadioButtonStyle.qml
|   |       |   |   |   |   |       |   |   RadioButtonStyle.qmlc
|   |       |   |   |   |   |       |   |   ScrollViewStyle.qml
|   |       |   |   |   |   |       |   |   ScrollViewStyle.qmlc
|   |       |   |   |   |   |       |   |   SliderStyle.qml
|   |       |   |   |   |   |       |   |   SliderStyle.qmlc
|   |       |   |   |   |   |       |   |   SpinBoxStyle.qml
|   |       |   |   |   |   |       |   |   SpinBoxStyle.qmlc
|   |       |   |   |   |   |       |   |   StatusBarStyle.qml
|   |       |   |   |   |   |       |   |   StatusBarStyle.qmlc
|   |       |   |   |   |   |       |   |   StatusIndicatorStyle.qml
|   |       |   |   |   |   |       |   |   StatusIndicatorStyle.qmlc
|   |       |   |   |   |   |       |   |   SwitchStyle.qml
|   |       |   |   |   |   |       |   |   SwitchStyle.qmlc
|   |       |   |   |   |   |       |   |   TableViewStyle.qml
|   |       |   |   |   |   |       |   |   TableViewStyle.qmlc
|   |       |   |   |   |   |       |   |   TabViewStyle.qml
|   |       |   |   |   |   |       |   |   TabViewStyle.qmlc
|   |       |   |   |   |   |       |   |   TextAreaStyle.qml
|   |       |   |   |   |   |       |   |   TextAreaStyle.qmlc
|   |       |   |   |   |   |       |   |   TextFieldStyle.qml
|   |       |   |   |   |   |       |   |   TextFieldStyle.qmlc
|   |       |   |   |   |   |       |   |   ToggleButtonStyle.qml
|   |       |   |   |   |   |       |   |   ToggleButtonStyle.qmlc
|   |       |   |   |   |   |       |   |   ToolBarStyle.qml
|   |       |   |   |   |   |       |   |   ToolBarStyle.qmlc
|   |       |   |   |   |   |       |   |   ToolButtonStyle.qml
|   |       |   |   |   |   |       |   |   ToolButtonStyle.qmlc
|   |       |   |   |   |   |       |   |   TreeViewStyle.qml
|   |       |   |   |   |   |       |   |   TreeViewStyle.qmlc
|   |       |   |   |   |   |       |   |   TumblerStyle.qml
|   |       |   |   |   |   |       |   |   TumblerStyle.qmlc
|   |       |   |   |   |   |       |   |   
|   |       |   |   |   |   |       |   \---images
|   |       |   |   |   |   |       |           arrow-down.png
|   |       |   |   |   |   |       |           arrow-down@2x.png
|   |       |   |   |   |   |       |           arrow-left.png
|   |       |   |   |   |   |       |           arrow-left@2x.png
|   |       |   |   |   |   |       |           arrow-right.png
|   |       |   |   |   |   |       |           arrow-right@2x.png
|   |       |   |   |   |   |       |           arrow-up.png
|   |       |   |   |   |   |       |           arrow-up@2x.png
|   |       |   |   |   |   |       |           button.png
|   |       |   |   |   |   |       |           button_down.png
|   |       |   |   |   |   |       |           check.png
|   |       |   |   |   |   |       |           check@2x.png
|   |       |   |   |   |   |       |           editbox.png
|   |       |   |   |   |   |       |           focusframe.png
|   |       |   |   |   |   |       |           groupbox.png
|   |       |   |   |   |   |       |           header.png
|   |       |   |   |   |   |       |           knob.png
|   |       |   |   |   |   |       |           leftanglearrow.png
|   |       |   |   |   |   |       |           needle.png
|   |       |   |   |   |   |       |           progress-indeterminate.png
|   |       |   |   |   |   |       |           rightanglearrow.png
|   |       |   |   |   |   |       |           scrollbar-handle-horizontal.png
|   |       |   |   |   |   |       |           scrollbar-handle-transient.png
|   |       |   |   |   |   |       |           scrollbar-handle-vertical.png
|   |       |   |   |   |   |       |           slider-groove.png
|   |       |   |   |   |   |       |           slider-handle.png
|   |       |   |   |   |   |       |           spinner_large.png
|   |       |   |   |   |   |       |           spinner_medium.png
|   |       |   |   |   |   |       |           spinner_small.png
|   |       |   |   |   |   |       |           tab.png
|   |       |   |   |   |   |       |           tab_selected.png
|   |       |   |   |   |   |       |           
|   |       |   |   |   |   |       +---Desktop
|   |       |   |   |   |   |       |       ApplicationWindowStyle.qml
|   |       |   |   |   |   |       |       ApplicationWindowStyle.qmlc
|   |       |   |   |   |   |       |       BusyIndicatorStyle.qml
|   |       |   |   |   |   |       |       BusyIndicatorStyle.qmlc
|   |       |   |   |   |   |       |       ButtonStyle.qml
|   |       |   |   |   |   |       |       ButtonStyle.qmlc
|   |       |   |   |   |   |       |       CalendarStyle.qml
|   |       |   |   |   |   |       |       CalendarStyle.qmlc
|   |       |   |   |   |   |       |       CheckBoxStyle.qml
|   |       |   |   |   |   |       |       CheckBoxStyle.qmlc
|   |       |   |   |   |   |       |       ComboBoxStyle.qml
|   |       |   |   |   |   |       |       ComboBoxStyle.qmlc
|   |       |   |   |   |   |       |       FocusFrameStyle.qml
|   |       |   |   |   |   |       |       FocusFrameStyle.qmlc
|   |       |   |   |   |   |       |       GroupBoxStyle.qml
|   |       |   |   |   |   |       |       GroupBoxStyle.qmlc
|   |       |   |   |   |   |       |       MenuBarStyle.qml
|   |       |   |   |   |   |       |       MenuBarStyle.qmlc
|   |       |   |   |   |   |       |       MenuStyle.qml
|   |       |   |   |   |   |       |       MenuStyle.qmlc
|   |       |   |   |   |   |       |       ProgressBarStyle.qml
|   |       |   |   |   |   |       |       ProgressBarStyle.qmlc
|   |       |   |   |   |   |       |       qmldir
|   |       |   |   |   |   |       |       RadioButtonStyle.qml
|   |       |   |   |   |   |       |       RadioButtonStyle.qmlc
|   |       |   |   |   |   |       |       RowItemSingleton.qml
|   |       |   |   |   |   |       |       RowItemSingleton.qmlc
|   |       |   |   |   |   |       |       ScrollViewStyle.qml
|   |       |   |   |   |   |       |       ScrollViewStyle.qmlc
|   |       |   |   |   |   |       |       SliderStyle.qml
|   |       |   |   |   |   |       |       SliderStyle.qmlc
|   |       |   |   |   |   |       |       SpinBoxStyle.qml
|   |       |   |   |   |   |       |       SpinBoxStyle.qmlc
|   |       |   |   |   |   |       |       StatusBarStyle.qml
|   |       |   |   |   |   |       |       StatusBarStyle.qmlc
|   |       |   |   |   |   |       |       SwitchStyle.qml
|   |       |   |   |   |   |       |       SwitchStyle.qmlc
|   |       |   |   |   |   |       |       TableViewStyle.qml
|   |       |   |   |   |   |       |       TableViewStyle.qmlc
|   |       |   |   |   |   |       |       TabViewStyle.qml
|   |       |   |   |   |   |       |       TabViewStyle.qmlc
|   |       |   |   |   |   |       |       TextAreaStyle.qml
|   |       |   |   |   |   |       |       TextAreaStyle.qmlc
|   |       |   |   |   |   |       |       TextFieldStyle.qml
|   |       |   |   |   |   |       |       TextFieldStyle.qmlc
|   |       |   |   |   |   |       |       ToolBarStyle.qml
|   |       |   |   |   |   |       |       ToolBarStyle.qmlc
|   |       |   |   |   |   |       |       ToolButtonStyle.qml
|   |       |   |   |   |   |       |       ToolButtonStyle.qmlc
|   |       |   |   |   |   |       |       TreeViewStyle.qml
|   |       |   |   |   |   |       |       TreeViewStyle.qmlc
|   |       |   |   |   |   |       |       
|   |       |   |   |   |   |       \---Flat
|   |       |   |   |   |   |               plugins.qmltypes
|   |       |   |   |   |   |               qmldir
|   |       |   |   |   |   |               qtquickextrasflatplugin.dll
|   |       |   |   |   |   |               
|   |       |   |   |   |   +---Controls.2
|   |       |   |   |   |   |   |   AbstractButton.qml
|   |       |   |   |   |   |   |   Action.qml
|   |       |   |   |   |   |   |   ActionGroup.qml
|   |       |   |   |   |   |   |   ApplicationWindow.qml
|   |       |   |   |   |   |   |   BusyIndicator.qml
|   |       |   |   |   |   |   |   Button.qml
|   |       |   |   |   |   |   |   ButtonGroup.qml
|   |       |   |   |   |   |   |   CheckBox.qml
|   |       |   |   |   |   |   |   CheckDelegate.qml
|   |       |   |   |   |   |   |   ComboBox.qml
|   |       |   |   |   |   |   |   Container.qml
|   |       |   |   |   |   |   |   Control.qml
|   |       |   |   |   |   |   |   DelayButton.qml
|   |       |   |   |   |   |   |   Dial.qml
|   |       |   |   |   |   |   |   Dialog.qml
|   |       |   |   |   |   |   |   DialogButtonBox.qml
|   |       |   |   |   |   |   |   Drawer.qml
|   |       |   |   |   |   |   |   Frame.qml
|   |       |   |   |   |   |   |   GroupBox.qml
|   |       |   |   |   |   |   |   HorizontalHeaderView.qml
|   |       |   |   |   |   |   |   ItemDelegate.qml
|   |       |   |   |   |   |   |   Label.qml
|   |       |   |   |   |   |   |   Menu.qml
|   |       |   |   |   |   |   |   MenuBar.qml
|   |       |   |   |   |   |   |   MenuBarItem.qml
|   |       |   |   |   |   |   |   MenuItem.qml
|   |       |   |   |   |   |   |   MenuSeparator.qml
|   |       |   |   |   |   |   |   Page.qml
|   |       |   |   |   |   |   |   PageIndicator.qml
|   |       |   |   |   |   |   |   Pane.qml
|   |       |   |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   |   Popup.qml
|   |       |   |   |   |   |   |   ProgressBar.qml
|   |       |   |   |   |   |   |   qmldir
|   |       |   |   |   |   |   |   qtquickcontrols2plugin.dll
|   |       |   |   |   |   |   |   RadioButton.qml
|   |       |   |   |   |   |   |   RadioDelegate.qml
|   |       |   |   |   |   |   |   RangeSlider.qml
|   |       |   |   |   |   |   |   RoundButton.qml
|   |       |   |   |   |   |   |   ScrollBar.qml
|   |       |   |   |   |   |   |   ScrollIndicator.qml
|   |       |   |   |   |   |   |   ScrollView.qml
|   |       |   |   |   |   |   |   Slider.qml
|   |       |   |   |   |   |   |   SpinBox.qml
|   |       |   |   |   |   |   |   SplitView.qml
|   |       |   |   |   |   |   |   StackView.qml
|   |       |   |   |   |   |   |   SwipeDelegate.qml
|   |       |   |   |   |   |   |   SwipeView.qml
|   |       |   |   |   |   |   |   Switch.qml
|   |       |   |   |   |   |   |   SwitchDelegate.qml
|   |       |   |   |   |   |   |   TabBar.qml
|   |       |   |   |   |   |   |   TabButton.qml
|   |       |   |   |   |   |   |   TextArea.qml
|   |       |   |   |   |   |   |   TextField.qml
|   |       |   |   |   |   |   |   ToolBar.qml
|   |       |   |   |   |   |   |   ToolButton.qml
|   |       |   |   |   |   |   |   ToolSeparator.qml
|   |       |   |   |   |   |   |   ToolTip.qml
|   |       |   |   |   |   |   |   Tumbler.qml
|   |       |   |   |   |   |   |   VerticalHeaderView.qml
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---designer
|   |       |   |   |   |   |   |   |   AbstractButtonSection.qml
|   |       |   |   |   |   |   |   |   BusyIndicatorSpecifics.qml
|   |       |   |   |   |   |   |   |   ButtonSection.qml
|   |       |   |   |   |   |   |   |   ButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   CheckBoxSpecifics.qml
|   |       |   |   |   |   |   |   |   CheckDelegateSpecifics.qml
|   |       |   |   |   |   |   |   |   CheckSection.qml
|   |       |   |   |   |   |   |   |   ComboBoxSpecifics.qml
|   |       |   |   |   |   |   |   |   ContainerSection.qml
|   |       |   |   |   |   |   |   |   ControlSection.qml
|   |       |   |   |   |   |   |   |   ControlSpecifics.qml
|   |       |   |   |   |   |   |   |   DelayButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   DialSpecifics.qml
|   |       |   |   |   |   |   |   |   FrameSpecifics.qml
|   |       |   |   |   |   |   |   |   GroupBoxSpecifics.qml
|   |       |   |   |   |   |   |   |   InsetSection.qml
|   |       |   |   |   |   |   |   |   ItemDelegateSection.qml
|   |       |   |   |   |   |   |   |   ItemDelegateSpecifics.qml
|   |       |   |   |   |   |   |   |   LabelSpecifics.qml
|   |       |   |   |   |   |   |   |   PaddingSection.qml
|   |       |   |   |   |   |   |   |   PageIndicatorSpecifics.qml
|   |       |   |   |   |   |   |   |   PageSpecifics.qml
|   |       |   |   |   |   |   |   |   PaneSection.qml
|   |       |   |   |   |   |   |   |   PaneSpecifics.qml
|   |       |   |   |   |   |   |   |   ProgressBarSpecifics.qml
|   |       |   |   |   |   |   |   |   qtquickcontrols2.metainfo
|   |       |   |   |   |   |   |   |   RadioButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   RadioDelegateSpecifics.qml
|   |       |   |   |   |   |   |   |   RangeSliderSpecifics.qml
|   |       |   |   |   |   |   |   |   RoundButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   ScrollViewSpecifics.qml
|   |       |   |   |   |   |   |   |   SliderSpecifics.qml
|   |       |   |   |   |   |   |   |   SpinBoxSpecifics.qml
|   |       |   |   |   |   |   |   |   StackViewSpecifics.qml
|   |       |   |   |   |   |   |   |   SwipeDelegateSpecifics.qml
|   |       |   |   |   |   |   |   |   SwipeViewSpecifics.qml
|   |       |   |   |   |   |   |   |   SwitchDelegateSpecifics.qml
|   |       |   |   |   |   |   |   |   SwitchSpecifics.qml
|   |       |   |   |   |   |   |   |   TabBarSpecifics.qml
|   |       |   |   |   |   |   |   |   TabButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   TextAreaSpecifics.qml
|   |       |   |   |   |   |   |   |   TextFieldSpecifics.qml
|   |       |   |   |   |   |   |   |   ToolBarSpecifics.qml
|   |       |   |   |   |   |   |   |   ToolButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   ToolSeparatorSpecifics.qml
|   |       |   |   |   |   |   |   |   TumblerSpecifics.qml
|   |       |   |   |   |   |   |   |   
|   |       |   |   |   |   |   |   \---images
|   |       |   |   |   |   |   |           busyindicator-icon.png
|   |       |   |   |   |   |   |           busyindicator-icon16.png
|   |       |   |   |   |   |   |           busyindicator-icon@2x.png
|   |       |   |   |   |   |   |           button-icon.png
|   |       |   |   |   |   |   |           button-icon16.png
|   |       |   |   |   |   |   |           button-icon@2x.png
|   |       |   |   |   |   |   |           checkbox-icon.png
|   |       |   |   |   |   |   |           checkbox-icon16.png
|   |       |   |   |   |   |   |           checkbox-icon@2x.png
|   |       |   |   |   |   |   |           combobox-icon.png
|   |       |   |   |   |   |   |           combobox-icon16.png
|   |       |   |   |   |   |   |           combobox-icon@2x.png
|   |       |   |   |   |   |   |           delaybutton-icon.png
|   |       |   |   |   |   |   |           delaybutton-icon16.png
|   |       |   |   |   |   |   |           delaybutton-icon@2x.png
|   |       |   |   |   |   |   |           dial-icon.png
|   |       |   |   |   |   |   |           dial-icon16.png
|   |       |   |   |   |   |   |           dial-icon@2x.png
|   |       |   |   |   |   |   |           frame-icon.png
|   |       |   |   |   |   |   |           frame-icon16.png
|   |       |   |   |   |   |   |           frame-icon@2x.png
|   |       |   |   |   |   |   |           groupbox-icon.png
|   |       |   |   |   |   |   |           groupbox-icon16.png
|   |       |   |   |   |   |   |           groupbox-icon@2x.png
|   |       |   |   |   |   |   |           itemdelegate-icon.png
|   |       |   |   |   |   |   |           itemdelegate-icon16.png
|   |       |   |   |   |   |   |           itemdelegate-icon@2x.png
|   |       |   |   |   |   |   |           label-icon.png
|   |       |   |   |   |   |   |           label-icon16.png
|   |       |   |   |   |   |   |           label-icon@2x.png
|   |       |   |   |   |   |   |           page-icon.png
|   |       |   |   |   |   |   |           page-icon16.png
|   |       |   |   |   |   |   |           page-icon@2x.png
|   |       |   |   |   |   |   |           pageindicator-icon.png
|   |       |   |   |   |   |   |           pageindicator-icon16.png
|   |       |   |   |   |   |   |           pageindicator-icon@2x.png
|   |       |   |   |   |   |   |           pane-icon.png
|   |       |   |   |   |   |   |           pane-icon16.png
|   |       |   |   |   |   |   |           pane-icon@2x.png
|   |       |   |   |   |   |   |           progressbar-icon.png
|   |       |   |   |   |   |   |           progressbar-icon16.png
|   |       |   |   |   |   |   |           progressbar-icon@2x.png
|   |       |   |   |   |   |   |           radiobutton-icon.png
|   |       |   |   |   |   |   |           radiobutton-icon16.png
|   |       |   |   |   |   |   |           radiobutton-icon@2x.png
|   |       |   |   |   |   |   |           rangeslider-icon.png
|   |       |   |   |   |   |   |           rangeslider-icon16.png
|   |       |   |   |   |   |   |           rangeslider-icon@2x.png
|   |       |   |   |   |   |   |           roundbutton-icon.png
|   |       |   |   |   |   |   |           roundbutton-icon16.png
|   |       |   |   |   |   |   |           roundbutton-icon@2x.png
|   |       |   |   |   |   |   |           scrollview-icon.png
|   |       |   |   |   |   |   |           scrollview-icon16.png
|   |       |   |   |   |   |   |           scrollview-icon@2x.png
|   |       |   |   |   |   |   |           slider-icon.png
|   |       |   |   |   |   |   |           slider-icon16.png
|   |       |   |   |   |   |   |           slider-icon@2x.png
|   |       |   |   |   |   |   |           spinbox-icon.png
|   |       |   |   |   |   |   |           spinbox-icon16.png
|   |       |   |   |   |   |   |           spinbox-icon@2x.png
|   |       |   |   |   |   |   |           stackview-icon.png
|   |       |   |   |   |   |   |           stackview-icon16.png
|   |       |   |   |   |   |   |           stackview-icon@2x.png
|   |       |   |   |   |   |   |           swipeview-icon.png
|   |       |   |   |   |   |   |           swipeview-icon16.png
|   |       |   |   |   |   |   |           swipeview-icon@2x.png
|   |       |   |   |   |   |   |           switch-icon.png
|   |       |   |   |   |   |   |           switch-icon16.png
|   |       |   |   |   |   |   |           switch-icon@2x.png
|   |       |   |   |   |   |   |           textarea-icon.png
|   |       |   |   |   |   |   |           textarea-icon16.png
|   |       |   |   |   |   |   |           textarea-icon@2x.png
|   |       |   |   |   |   |   |           textfield-icon.png
|   |       |   |   |   |   |   |           textfield-icon16.png
|   |       |   |   |   |   |   |           textfield-icon@2x.png
|   |       |   |   |   |   |   |           toolbar-icon.png
|   |       |   |   |   |   |   |           toolbar-icon16.png
|   |       |   |   |   |   |   |           toolbar-icon@2x.png
|   |       |   |   |   |   |   |           toolbutton-icon.png
|   |       |   |   |   |   |   |           toolbutton-icon16.png
|   |       |   |   |   |   |   |           toolbutton-icon@2x.png
|   |       |   |   |   |   |   |           toolseparator-icon.png
|   |       |   |   |   |   |   |           toolseparator-icon16.png
|   |       |   |   |   |   |   |           toolseparator-icon@2x.png
|   |       |   |   |   |   |   |           tumbler-icon.png
|   |       |   |   |   |   |   |           tumbler-icon16.png
|   |       |   |   |   |   |   |           tumbler-icon@2x.png
|   |       |   |   |   |   |   |           
|   |       |   |   |   |   |   +---Fusion
|   |       |   |   |   |   |   |       ApplicationWindow.qml
|   |       |   |   |   |   |   |       BusyIndicator.qml
|   |       |   |   |   |   |   |       Button.qml
|   |       |   |   |   |   |   |       ButtonPanel.qml
|   |       |   |   |   |   |   |       CheckBox.qml
|   |       |   |   |   |   |   |       CheckDelegate.qml
|   |       |   |   |   |   |   |       CheckIndicator.qml
|   |       |   |   |   |   |   |       ComboBox.qml
|   |       |   |   |   |   |   |       DelayButton.qml
|   |       |   |   |   |   |   |       Dial.qml
|   |       |   |   |   |   |   |       Dialog.qml
|   |       |   |   |   |   |   |       DialogButtonBox.qml
|   |       |   |   |   |   |   |       Drawer.qml
|   |       |   |   |   |   |   |       Frame.qml
|   |       |   |   |   |   |   |       GroupBox.qml
|   |       |   |   |   |   |   |       HorizontalHeaderView.qml
|   |       |   |   |   |   |   |       ItemDelegate.qml
|   |       |   |   |   |   |   |       Label.qml
|   |       |   |   |   |   |   |       Menu.qml
|   |       |   |   |   |   |   |       MenuBar.qml
|   |       |   |   |   |   |   |       MenuBarItem.qml
|   |       |   |   |   |   |   |       MenuItem.qml
|   |       |   |   |   |   |   |       MenuSeparator.qml
|   |       |   |   |   |   |   |       Page.qml
|   |       |   |   |   |   |   |       PageIndicator.qml
|   |       |   |   |   |   |   |       Pane.qml
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       Popup.qml
|   |       |   |   |   |   |   |       ProgressBar.qml
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qtquickcontrols2fusionstyleplugin.dll
|   |       |   |   |   |   |   |       RadioButton.qml
|   |       |   |   |   |   |   |       RadioDelegate.qml
|   |       |   |   |   |   |   |       RadioIndicator.qml
|   |       |   |   |   |   |   |       RangeSlider.qml
|   |       |   |   |   |   |   |       RoundButton.qml
|   |       |   |   |   |   |   |       ScrollBar.qml
|   |       |   |   |   |   |   |       ScrollIndicator.qml
|   |       |   |   |   |   |   |       Slider.qml
|   |       |   |   |   |   |   |       SliderGroove.qml
|   |       |   |   |   |   |   |       SliderHandle.qml
|   |       |   |   |   |   |   |       SpinBox.qml
|   |       |   |   |   |   |   |       SplitView.qml
|   |       |   |   |   |   |   |       SwipeDelegate.qml
|   |       |   |   |   |   |   |       Switch.qml
|   |       |   |   |   |   |   |       SwitchDelegate.qml
|   |       |   |   |   |   |   |       SwitchIndicator.qml
|   |       |   |   |   |   |   |       TabBar.qml
|   |       |   |   |   |   |   |       TabButton.qml
|   |       |   |   |   |   |   |       TextArea.qml
|   |       |   |   |   |   |   |       TextField.qml
|   |       |   |   |   |   |   |       ToolBar.qml
|   |       |   |   |   |   |   |       ToolButton.qml
|   |       |   |   |   |   |   |       ToolSeparator.qml
|   |       |   |   |   |   |   |       ToolTip.qml
|   |       |   |   |   |   |   |       Tumbler.qml
|   |       |   |   |   |   |   |       VerticalHeaderView.qml
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---Imagine
|   |       |   |   |   |   |   |       ApplicationWindow.qml
|   |       |   |   |   |   |   |       BusyIndicator.qml
|   |       |   |   |   |   |   |       Button.qml
|   |       |   |   |   |   |   |       CheckBox.qml
|   |       |   |   |   |   |   |       CheckDelegate.qml
|   |       |   |   |   |   |   |       ComboBox.qml
|   |       |   |   |   |   |   |       DelayButton.qml
|   |       |   |   |   |   |   |       Dial.qml
|   |       |   |   |   |   |   |       Dialog.qml
|   |       |   |   |   |   |   |       DialogButtonBox.qml
|   |       |   |   |   |   |   |       Drawer.qml
|   |       |   |   |   |   |   |       Frame.qml
|   |       |   |   |   |   |   |       GroupBox.qml
|   |       |   |   |   |   |   |       HorizontalHeaderView.qml
|   |       |   |   |   |   |   |       ItemDelegate.qml
|   |       |   |   |   |   |   |       Label.qml
|   |       |   |   |   |   |   |       Menu.qml
|   |       |   |   |   |   |   |       MenuItem.qml
|   |       |   |   |   |   |   |       MenuSeparator.qml
|   |       |   |   |   |   |   |       Page.qml
|   |       |   |   |   |   |   |       PageIndicator.qml
|   |       |   |   |   |   |   |       Pane.qml
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       Popup.qml
|   |       |   |   |   |   |   |       ProgressBar.qml
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qtquickcontrols2imaginestyleplugin.dll
|   |       |   |   |   |   |   |       RadioButton.qml
|   |       |   |   |   |   |   |       RadioDelegate.qml
|   |       |   |   |   |   |   |       RangeSlider.qml
|   |       |   |   |   |   |   |       RoundButton.qml
|   |       |   |   |   |   |   |       ScrollBar.qml
|   |       |   |   |   |   |   |       ScrollIndicator.qml
|   |       |   |   |   |   |   |       Slider.qml
|   |       |   |   |   |   |   |       SpinBox.qml
|   |       |   |   |   |   |   |       SplitView.qml
|   |       |   |   |   |   |   |       StackView.qml
|   |       |   |   |   |   |   |       SwipeDelegate.qml
|   |       |   |   |   |   |   |       SwipeView.qml
|   |       |   |   |   |   |   |       Switch.qml
|   |       |   |   |   |   |   |       SwitchDelegate.qml
|   |       |   |   |   |   |   |       TabBar.qml
|   |       |   |   |   |   |   |       TabButton.qml
|   |       |   |   |   |   |   |       TextArea.qml
|   |       |   |   |   |   |   |       TextField.qml
|   |       |   |   |   |   |   |       ToolBar.qml
|   |       |   |   |   |   |   |       ToolButton.qml
|   |       |   |   |   |   |   |       ToolSeparator.qml
|   |       |   |   |   |   |   |       ToolTip.qml
|   |       |   |   |   |   |   |       Tumbler.qml
|   |       |   |   |   |   |   |       VerticalHeaderView.qml
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---Material
|   |       |   |   |   |   |   |       ApplicationWindow.qml
|   |       |   |   |   |   |   |       BoxShadow.qml
|   |       |   |   |   |   |   |       BusyIndicator.qml
|   |       |   |   |   |   |   |       Button.qml
|   |       |   |   |   |   |   |       CheckBox.qml
|   |       |   |   |   |   |   |       CheckDelegate.qml
|   |       |   |   |   |   |   |       CheckIndicator.qml
|   |       |   |   |   |   |   |       ComboBox.qml
|   |       |   |   |   |   |   |       CursorDelegate.qml
|   |       |   |   |   |   |   |       DelayButton.qml
|   |       |   |   |   |   |   |       Dial.qml
|   |       |   |   |   |   |   |       Dialog.qml
|   |       |   |   |   |   |   |       DialogButtonBox.qml
|   |       |   |   |   |   |   |       Drawer.qml
|   |       |   |   |   |   |   |       ElevationEffect.qml
|   |       |   |   |   |   |   |       Frame.qml
|   |       |   |   |   |   |   |       GroupBox.qml
|   |       |   |   |   |   |   |       HorizontalHeaderView.qml
|   |       |   |   |   |   |   |       ItemDelegate.qml
|   |       |   |   |   |   |   |       Label.qml
|   |       |   |   |   |   |   |       Menu.qml
|   |       |   |   |   |   |   |       MenuBar.qml
|   |       |   |   |   |   |   |       MenuBarItem.qml
|   |       |   |   |   |   |   |       MenuItem.qml
|   |       |   |   |   |   |   |       MenuSeparator.qml
|   |       |   |   |   |   |   |       Page.qml
|   |       |   |   |   |   |   |       PageIndicator.qml
|   |       |   |   |   |   |   |       Pane.qml
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       Popup.qml
|   |       |   |   |   |   |   |       ProgressBar.qml
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       qtquickcontrols2materialstyleplugin.dll
|   |       |   |   |   |   |   |       RadioButton.qml
|   |       |   |   |   |   |   |       RadioDelegate.qml
|   |       |   |   |   |   |   |       RadioIndicator.qml
|   |       |   |   |   |   |   |       RangeSlider.qml
|   |       |   |   |   |   |   |       RectangularGlow.qml
|   |       |   |   |   |   |   |       RoundButton.qml
|   |       |   |   |   |   |   |       ScrollBar.qml
|   |       |   |   |   |   |   |       ScrollIndicator.qml
|   |       |   |   |   |   |   |       Slider.qml
|   |       |   |   |   |   |   |       SliderHandle.qml
|   |       |   |   |   |   |   |       SpinBox.qml
|   |       |   |   |   |   |   |       SplitView.qml
|   |       |   |   |   |   |   |       StackView.qml
|   |       |   |   |   |   |   |       SwipeDelegate.qml
|   |       |   |   |   |   |   |       SwipeView.qml
|   |       |   |   |   |   |   |       Switch.qml
|   |       |   |   |   |   |   |       SwitchDelegate.qml
|   |       |   |   |   |   |   |       SwitchIndicator.qml
|   |       |   |   |   |   |   |       TabBar.qml
|   |       |   |   |   |   |   |       TabButton.qml
|   |       |   |   |   |   |   |       TextArea.qml
|   |       |   |   |   |   |   |       TextField.qml
|   |       |   |   |   |   |   |       ToolBar.qml
|   |       |   |   |   |   |   |       ToolButton.qml
|   |       |   |   |   |   |   |       ToolSeparator.qml
|   |       |   |   |   |   |   |       ToolTip.qml
|   |       |   |   |   |   |   |       Tumbler.qml
|   |       |   |   |   |   |   |       VerticalHeaderView.qml
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   \---Universal
|   |       |   |   |   |   |           ApplicationWindow.qml
|   |       |   |   |   |   |           BusyIndicator.qml
|   |       |   |   |   |   |           Button.qml
|   |       |   |   |   |   |           CheckBox.qml
|   |       |   |   |   |   |           CheckDelegate.qml
|   |       |   |   |   |   |           CheckIndicator.qml
|   |       |   |   |   |   |           ComboBox.qml
|   |       |   |   |   |   |           DelayButton.qml
|   |       |   |   |   |   |           Dial.qml
|   |       |   |   |   |   |           Dialog.qml
|   |       |   |   |   |   |           DialogButtonBox.qml
|   |       |   |   |   |   |           Drawer.qml
|   |       |   |   |   |   |           Frame.qml
|   |       |   |   |   |   |           GroupBox.qml
|   |       |   |   |   |   |           HorizontalHeaderView.qml
|   |       |   |   |   |   |           ItemDelegate.qml
|   |       |   |   |   |   |           Label.qml
|   |       |   |   |   |   |           Menu.qml
|   |       |   |   |   |   |           MenuBar.qml
|   |       |   |   |   |   |           MenuBarItem.qml
|   |       |   |   |   |   |           MenuItem.qml
|   |       |   |   |   |   |           MenuSeparator.qml
|   |       |   |   |   |   |           Page.qml
|   |       |   |   |   |   |           PageIndicator.qml
|   |       |   |   |   |   |           Pane.qml
|   |       |   |   |   |   |           plugins.qmltypes
|   |       |   |   |   |   |           Popup.qml
|   |       |   |   |   |   |           ProgressBar.qml
|   |       |   |   |   |   |           qmldir
|   |       |   |   |   |   |           qtquickcontrols2universalstyleplugin.dll
|   |       |   |   |   |   |           RadioButton.qml
|   |       |   |   |   |   |           RadioDelegate.qml
|   |       |   |   |   |   |           RadioIndicator.qml
|   |       |   |   |   |   |           RangeSlider.qml
|   |       |   |   |   |   |           RoundButton.qml
|   |       |   |   |   |   |           ScrollBar.qml
|   |       |   |   |   |   |           ScrollIndicator.qml
|   |       |   |   |   |   |           Slider.qml
|   |       |   |   |   |   |           SpinBox.qml
|   |       |   |   |   |   |           SplitView.qml
|   |       |   |   |   |   |           StackView.qml
|   |       |   |   |   |   |           SwipeDelegate.qml
|   |       |   |   |   |   |           Switch.qml
|   |       |   |   |   |   |           SwitchDelegate.qml
|   |       |   |   |   |   |           SwitchIndicator.qml
|   |       |   |   |   |   |           TabBar.qml
|   |       |   |   |   |   |           TabButton.qml
|   |       |   |   |   |   |           TextArea.qml
|   |       |   |   |   |   |           TextField.qml
|   |       |   |   |   |   |           ToolBar.qml
|   |       |   |   |   |   |           ToolButton.qml
|   |       |   |   |   |   |           ToolSeparator.qml
|   |       |   |   |   |   |           ToolTip.qml
|   |       |   |   |   |   |           Tumbler.qml
|   |       |   |   |   |   |           VerticalHeaderView.qml
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---Dialogs
|   |       |   |   |   |   |   |   DefaultColorDialog.qml
|   |       |   |   |   |   |   |   DefaultColorDialog.qmlc
|   |       |   |   |   |   |   |   DefaultDialogWrapper.qml
|   |       |   |   |   |   |   |   DefaultDialogWrapper.qmlc
|   |       |   |   |   |   |   |   DefaultFileDialog.qml
|   |       |   |   |   |   |   |   DefaultFileDialog.qmlc
|   |       |   |   |   |   |   |   DefaultFontDialog.qml
|   |       |   |   |   |   |   |   DefaultFontDialog.qmlc
|   |       |   |   |   |   |   |   DefaultMessageDialog.qml
|   |       |   |   |   |   |   |   DefaultMessageDialog.qmlc
|   |       |   |   |   |   |   |   dialogplugin.dll
|   |       |   |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   |   qmldir
|   |       |   |   |   |   |   |   WidgetColorDialog.qml
|   |       |   |   |   |   |   |   WidgetColorDialog.qmlc
|   |       |   |   |   |   |   |   WidgetFileDialog.qml
|   |       |   |   |   |   |   |   WidgetFileDialog.qmlc
|   |       |   |   |   |   |   |   WidgetFontDialog.qml
|   |       |   |   |   |   |   |   WidgetFontDialog.qmlc
|   |       |   |   |   |   |   |   WidgetMessageDialog.qml
|   |       |   |   |   |   |   |   WidgetMessageDialog.qmlc
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---images
|   |       |   |   |   |   |   |       checkers.png
|   |       |   |   |   |   |   |       checkmark.png
|   |       |   |   |   |   |   |       copy.png
|   |       |   |   |   |   |   |       critical.png
|   |       |   |   |   |   |   |       crosshairs.png
|   |       |   |   |   |   |   |       information.png
|   |       |   |   |   |   |   |       question.png
|   |       |   |   |   |   |   |       slider_handle.png
|   |       |   |   |   |   |   |       sunken_frame.png
|   |       |   |   |   |   |   |       warning.png
|   |       |   |   |   |   |   |       window_border.png
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   +---Private
|   |       |   |   |   |   |   |       dialogsprivateplugin.dll
|   |       |   |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |   |       qmldir
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   \---qml
|   |       |   |   |   |   |           ColorSlider.qml
|   |       |   |   |   |   |           ColorSlider.qmlc
|   |       |   |   |   |   |           DefaultWindowDecoration.qml
|   |       |   |   |   |   |           DefaultWindowDecoration.qmlc
|   |       |   |   |   |   |           IconButtonStyle.qml
|   |       |   |   |   |   |           IconButtonStyle.qmlc
|   |       |   |   |   |   |           IconGlyph.qml
|   |       |   |   |   |   |           IconGlyph.qmlc
|   |       |   |   |   |   |           icons.ttf
|   |       |   |   |   |   |           qmldir
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---Extras
|   |       |   |   |   |   |   |   CircularGauge.qml
|   |       |   |   |   |   |   |   CircularGauge.qmlc
|   |       |   |   |   |   |   |   DelayButton.qml
|   |       |   |   |   |   |   |   DelayButton.qmlc
|   |       |   |   |   |   |   |   Dial.qml
|   |       |   |   |   |   |   |   Dial.qmlc
|   |       |   |   |   |   |   |   Gauge.qml
|   |       |   |   |   |   |   |   Gauge.qmlc
|   |       |   |   |   |   |   |   PieMenu.qml
|   |       |   |   |   |   |   |   PieMenu.qmlc
|   |       |   |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   |   qmldir
|   |       |   |   |   |   |   |   qtquickextrasplugin.dll
|   |       |   |   |   |   |   |   StatusIndicator.qml
|   |       |   |   |   |   |   |   StatusIndicator.qmlc
|   |       |   |   |   |   |   |   ToggleButton.qml
|   |       |   |   |   |   |   |   ToggleButton.qmlc
|   |       |   |   |   |   |   |   Tumbler.qml
|   |       |   |   |   |   |   |   Tumbler.qmlc
|   |       |   |   |   |   |   |   TumblerColumn.qml
|   |       |   |   |   |   |   |   TumblerColumn.qmlc
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---designer
|   |       |   |   |   |   |   |   |   CircularGaugeSpecifics.qml
|   |       |   |   |   |   |   |   |   CircularGaugeSpecifics.qmlc
|   |       |   |   |   |   |   |   |   DelayButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   DelayButtonSpecifics.qmlc
|   |       |   |   |   |   |   |   |   DialSpecifics.qml
|   |       |   |   |   |   |   |   |   DialSpecifics.qmlc
|   |       |   |   |   |   |   |   |   GaugeSpecifics.qml
|   |       |   |   |   |   |   |   |   GaugeSpecifics.qmlc
|   |       |   |   |   |   |   |   |   PictureSpecifics.qml
|   |       |   |   |   |   |   |   |   PictureSpecifics.qmlc
|   |       |   |   |   |   |   |   |   PieMenuSpecifics.qml
|   |       |   |   |   |   |   |   |   PieMenuSpecifics.qmlc
|   |       |   |   |   |   |   |   |   qtquickextras.metainfo
|   |       |   |   |   |   |   |   |   StatusIndicatorSpecifics.qml
|   |       |   |   |   |   |   |   |   StatusIndicatorSpecifics.qmlc
|   |       |   |   |   |   |   |   |   ToggleButtonSpecifics.qml
|   |       |   |   |   |   |   |   |   ToggleButtonSpecifics.qmlc
|   |       |   |   |   |   |   |   |   
|   |       |   |   |   |   |   |   \---images
|   |       |   |   |   |   |   |           circulargauge-icon.png
|   |       |   |   |   |   |   |           circulargauge-icon16.png
|   |       |   |   |   |   |   |           delaybutton-icon.png
|   |       |   |   |   |   |   |           delaybutton-icon16.png
|   |       |   |   |   |   |   |           dial-icon.png
|   |       |   |   |   |   |   |           dial-icon16.png
|   |       |   |   |   |   |   |           gauge-icon.png
|   |       |   |   |   |   |   |           gauge-icon16.png
|   |       |   |   |   |   |   |           picture-icon.png
|   |       |   |   |   |   |   |           picture-icon16.png
|   |       |   |   |   |   |   |           piemenu-icon.png
|   |       |   |   |   |   |   |           piemenu-icon16.png
|   |       |   |   |   |   |   |           statusindicator-icon.png
|   |       |   |   |   |   |   |           statusindicator-icon16.png
|   |       |   |   |   |   |   |           togglebutton-icon.png
|   |       |   |   |   |   |   |           togglebutton-icon16.png
|   |       |   |   |   |   |   |           tumbler-icon.png
|   |       |   |   |   |   |   |           tumbler-icon16.png
|   |       |   |   |   |   |   |           
|   |       |   |   |   |   |   \---Private
|   |       |   |   |   |   |           CircularButton.qml
|   |       |   |   |   |   |           CircularButton.qmlc
|   |       |   |   |   |   |           CircularButtonStyleHelper.qml
|   |       |   |   |   |   |           CircularButtonStyleHelper.qmlc
|   |       |   |   |   |   |           CircularTickmarkLabel.qml
|   |       |   |   |   |   |           CircularTickmarkLabel.qmlc
|   |       |   |   |   |   |           Handle.qml
|   |       |   |   |   |   |           Handle.qmlc
|   |       |   |   |   |   |           PieMenuIcon.qml
|   |       |   |   |   |   |           PieMenuIcon.qmlc
|   |       |   |   |   |   |           qmldir
|   |       |   |   |   |   |           TextSingleton.qml
|   |       |   |   |   |   |           TextSingleton.qmlc
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---Layouts
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qquicklayoutsplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---LocalStorage
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qmllocalstorageplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Particles.2
|   |       |   |   |   |   |       particlesplugin.dll
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---PrivateWidgets
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       widgetsplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Scene2D
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qtquickscene2dplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Scene3D
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qtquickscene3dplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Shapes
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qmlshapesplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Templates.2
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qtquicktemplates2plugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Timeline
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       qtquicktimelineplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---Window.2
|   |       |   |   |   |   |       plugins.qmltypes
|   |       |   |   |   |   |       qmldir
|   |       |   |   |   |   |       windowplugin.dll
|   |       |   |   |   |   |       
|   |       |   |   |   |   \---XmlListModel
|   |       |   |   |   |           plugins.qmltypes
|   |       |   |   |   |           qmldir
|   |       |   |   |   |           qmlxmllistmodelplugin.dll
|   |       |   |   |   |           
|   |       |   |   |   +---QtQuick.2
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       qtquick2plugin.dll
|   |       |   |   |   |       
|   |       |   |   |   +---QtQuick3D
|   |       |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   qmldir
|   |       |   |   |   |   |   qquick3dplugin.dll
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---designer
|   |       |   |   |   |   |   |   AreaLightSection.qml
|   |       |   |   |   |   |   |   AreaLightSpecifics.qml
|   |       |   |   |   |   |   |   BlendingSection.qml
|   |       |   |   |   |   |   |   BlendingSpecifics.qml
|   |       |   |   |   |   |   |   BufferBlitSection.qml
|   |       |   |   |   |   |   |   BufferBlitSpecifics.qml
|   |       |   |   |   |   |   |   BufferInputSection.qml
|   |       |   |   |   |   |   |   BufferInputSpecifics.qml
|   |       |   |   |   |   |   |   BufferSection.qml
|   |       |   |   |   |   |   |   BufferSpecifics.qml
|   |       |   |   |   |   |   |   CullModeSection.qml
|   |       |   |   |   |   |   |   CullModeSpecifics.qml
|   |       |   |   |   |   |   |   CustomCameraSection.qml
|   |       |   |   |   |   |   |   CustomCameraSpecifics.qml
|   |       |   |   |   |   |   |   DefaultMaterialSection.qml
|   |       |   |   |   |   |   |   DefaultMaterialSpecifics.qml
|   |       |   |   |   |   |   |   DepthInputSection.qml
|   |       |   |   |   |   |   |   DepthInputSpecifics.qml
|   |       |   |   |   |   |   |   DirectionalLightSection.qml
|   |       |   |   |   |   |   |   DirectionalLightSpecifics.qml
|   |       |   |   |   |   |   |   FrustumCameraSection.qml
|   |       |   |   |   |   |   |   FrustumCameraSpecifics.qml
|   |       |   |   |   |   |   |   IdComboBox.qml
|   |       |   |   |   |   |   |   MaterialSection.qml
|   |       |   |   |   |   |   |   ModelSection.qml
|   |       |   |   |   |   |   |   ModelSpecifics.qml
|   |       |   |   |   |   |   |   NodeSection.qml
|   |       |   |   |   |   |   |   NodeSpecifics.qml
|   |       |   |   |   |   |   |   Object3DSection.qml
|   |       |   |   |   |   |   |   OrthographicCameraSection.qml
|   |       |   |   |   |   |   |   OrthographicCameraSpecifics.qml
|   |       |   |   |   |   |   |   PassSection.qml
|   |       |   |   |   |   |   |   PassSpecifics.qml
|   |       |   |   |   |   |   |   PerspectiveCameraSection.qml
|   |       |   |   |   |   |   |   PerspectiveCameraSpecifics.qml
|   |       |   |   |   |   |   |   PointLightSection.qml
|   |       |   |   |   |   |   |   PointLightSpecifics.qml
|   |       |   |   |   |   |   |   PrincipledMaterialSection.qml
|   |       |   |   |   |   |   |   PrincipledMaterialSpecifics.qml
|   |       |   |   |   |   |   |   quick3d.metainfo
|   |       |   |   |   |   |   |   RenderStateSection.qml
|   |       |   |   |   |   |   |   RenderStateSpecifics.qml
|   |       |   |   |   |   |   |   SceneEnvironmentSection.qml
|   |       |   |   |   |   |   |   SceneEnvironmentSpecifics.qml
|   |       |   |   |   |   |   |   SetUniformValueSection.qml
|   |       |   |   |   |   |   |   SetUniformValueSpecifics.qml
|   |       |   |   |   |   |   |   ShaderInfoSection.qml
|   |       |   |   |   |   |   |   ShaderInfoSpecifics.qml
|   |       |   |   |   |   |   |   ShaderSection.qml
|   |       |   |   |   |   |   |   ShaderSpecifics.qml
|   |       |   |   |   |   |   |   ShadowSection.qml
|   |       |   |   |   |   |   |   SpotLightSection.qml
|   |       |   |   |   |   |   |   SpotLightSpecifics.qml
|   |       |   |   |   |   |   |   TextureInputSection.qml
|   |       |   |   |   |   |   |   TextureInputSpecifics.qml
|   |       |   |   |   |   |   |   TextureSection.qml
|   |       |   |   |   |   |   |   TextureSpecifics.qml
|   |       |   |   |   |   |   |   View3DSection.qml
|   |       |   |   |   |   |   |   View3DSpecifics.qml
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---images
|   |       |   |   |   |   |   |       camera.png
|   |       |   |   |   |   |   |       camera16.png
|   |       |   |   |   |   |   |       camera@2x.png
|   |       |   |   |   |   |   |       cone.png
|   |       |   |   |   |   |   |       cone16.png
|   |       |   |   |   |   |   |       cone@2x.png
|   |       |   |   |   |   |   |       cube.png
|   |       |   |   |   |   |   |       cube16.png
|   |       |   |   |   |   |   |       cube@2x.png
|   |       |   |   |   |   |   |       cylinder.png
|   |       |   |   |   |   |   |       cylinder16.png
|   |       |   |   |   |   |   |       cylinder@2x.png
|   |       |   |   |   |   |   |       dummy.png
|   |       |   |   |   |   |   |       dummy16.png
|   |       |   |   |   |   |   |       dummy@2x.png
|   |       |   |   |   |   |   |       group.png
|   |       |   |   |   |   |   |       group16.png
|   |       |   |   |   |   |   |       group@2x.png
|   |       |   |   |   |   |   |       light.png
|   |       |   |   |   |   |   |       light16.png
|   |       |   |   |   |   |   |       light@2x.png
|   |       |   |   |   |   |   |       material.png
|   |       |   |   |   |   |   |       material16.png
|   |       |   |   |   |   |   |       material@2x.png
|   |       |   |   |   |   |   |       model16.png
|   |       |   |   |   |   |   |       plane.png
|   |       |   |   |   |   |   |       plane16.png
|   |       |   |   |   |   |   |       plane@2x.png
|   |       |   |   |   |   |   |       scene.png
|   |       |   |   |   |   |   |       scene16.png
|   |       |   |   |   |   |   |       scene@2x.png
|   |       |   |   |   |   |   |       shadercommand.png
|   |       |   |   |   |   |   |       shadercommand16.png
|   |       |   |   |   |   |   |       shadercommand@2x.png
|   |       |   |   |   |   |   |       shaderutil.png
|   |       |   |   |   |   |   |       shaderutil16.png
|   |       |   |   |   |   |   |       shaderutil@2x.png
|   |       |   |   |   |   |   |       sphere.png
|   |       |   |   |   |   |   |       sphere16.png
|   |       |   |   |   |   |   |       sphere@2x.png
|   |       |   |   |   |   |   |       texture.png
|   |       |   |   |   |   |   |       texture16.png
|   |       |   |   |   |   |   |       texture@2x.png
|   |       |   |   |   |   |   |       view3D.png
|   |       |   |   |   |   |   |       view3D16.png
|   |       |   |   |   |   |   |       view3D@2x.png
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   \---source
|   |       |   |   |   |   |           cone_model_template.qml
|   |       |   |   |   |   |           cube_model_template.qml
|   |       |   |   |   |   |           cylinder_model_template.qml
|   |       |   |   |   |   |           plane_model_template.qml
|   |       |   |   |   |   |           sphere_model_template.qml
|   |       |   |   |   |   |           view3D_template.qml
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---Effects
|   |       |   |   |   |   |   |   AdditiveColorGradient.qml
|   |       |   |   |   |   |   |   Blur.qml
|   |       |   |   |   |   |   |   BrushStrokes.qml
|   |       |   |   |   |   |   |   ChromaticAberration.qml
|   |       |   |   |   |   |   |   ColorMaster.qml
|   |       |   |   |   |   |   |   DepthOfFieldHQBlur.qml
|   |       |   |   |   |   |   |   Desaturate.qml
|   |       |   |   |   |   |   |   DistortionRipple.qml
|   |       |   |   |   |   |   |   DistortionSphere.qml
|   |       |   |   |   |   |   |   DistortionSpiral.qml
|   |       |   |   |   |   |   |   EdgeDetect.qml
|   |       |   |   |   |   |   |   Emboss.qml
|   |       |   |   |   |   |   |   Flip.qml
|   |       |   |   |   |   |   |   Fxaa.qml
|   |       |   |   |   |   |   |   GaussianBlur.qml
|   |       |   |   |   |   |   |   HDRBloomTonemap.qml
|   |       |   |   |   |   |   |   MotionBlur.qml
|   |       |   |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   |   qmldir
|   |       |   |   |   |   |   |   qtquick3deffectplugin.dll
|   |       |   |   |   |   |   |   Scatter.qml
|   |       |   |   |   |   |   |   SCurveTonemap.qml
|   |       |   |   |   |   |   |   TiltShift.qml
|   |       |   |   |   |   |   |   Vignette.qml
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---designer
|   |       |   |   |   |   |   |   |   AdditiveColorGradientSection.qml
|   |       |   |   |   |   |   |   |   AdditiveColorGradientSpecifics.qml
|   |       |   |   |   |   |   |   |   BlurSection.qml
|   |       |   |   |   |   |   |   |   BlurSpecifics.qml
|   |       |   |   |   |   |   |   |   BrushStrokesSection.qml
|   |       |   |   |   |   |   |   |   BrushStrokesSpecifics.qml
|   |       |   |   |   |   |   |   |   ChromaticAberrationSection.qml
|   |       |   |   |   |   |   |   |   ChromaticAberrationSpecifics.qml
|   |       |   |   |   |   |   |   |   ColorMasterSection.qml
|   |       |   |   |   |   |   |   |   ColorMasterSpecifics.qml
|   |       |   |   |   |   |   |   |   DepthOfFieldHQBlurSection.qml
|   |       |   |   |   |   |   |   |   DepthOfFieldHQBlurSpecifics.qml
|   |       |   |   |   |   |   |   |   DesaturateSection.qml
|   |       |   |   |   |   |   |   |   DesaturateSpecifics.qml
|   |       |   |   |   |   |   |   |   DistortionRippleSection.qml
|   |       |   |   |   |   |   |   |   DistortionRippleSpecifics.qml
|   |       |   |   |   |   |   |   |   DistortionSphereSection.qml
|   |       |   |   |   |   |   |   |   DistortionSphereSpecifics.qml
|   |       |   |   |   |   |   |   |   DistortionSpiralSection.qml
|   |       |   |   |   |   |   |   |   DistortionSpiralSpecifics.qml
|   |       |   |   |   |   |   |   |   EdgeDetectSection.qml
|   |       |   |   |   |   |   |   |   EdgeDetectSpecifics.qml
|   |       |   |   |   |   |   |   |   effectlib.metainfo
|   |       |   |   |   |   |   |   |   EffectSection.qml
|   |       |   |   |   |   |   |   |   EffectSpecifics.qml
|   |       |   |   |   |   |   |   |   EmbossSection.qml
|   |       |   |   |   |   |   |   |   EmbossSpecifics.qml
|   |       |   |   |   |   |   |   |   FlipSection.qml
|   |       |   |   |   |   |   |   |   FlipSpecifics.qml
|   |       |   |   |   |   |   |   |   FxaaSection.qml
|   |       |   |   |   |   |   |   |   FxaaSpecifics.qml
|   |       |   |   |   |   |   |   |   GaussianBlurSection.qml
|   |       |   |   |   |   |   |   |   GaussianBlurSpecifics.qml
|   |       |   |   |   |   |   |   |   HDRBloomTonemapSection.qml
|   |       |   |   |   |   |   |   |   HDRBloomTonemapSpecifics.qml
|   |       |   |   |   |   |   |   |   IdComboBox.qml
|   |       |   |   |   |   |   |   |   MotionBlurSection.qml
|   |       |   |   |   |   |   |   |   MotionBlurSpecifics.qml
|   |       |   |   |   |   |   |   |   ScatterSection.qml
|   |       |   |   |   |   |   |   |   ScatterSpecifics.qml
|   |       |   |   |   |   |   |   |   SCurveTonemapSection.qml
|   |       |   |   |   |   |   |   |   SCurveTonemapSpecifics.qml
|   |       |   |   |   |   |   |   |   TiltShiftSection.qml
|   |       |   |   |   |   |   |   |   TiltShiftSpecifics.qml
|   |       |   |   |   |   |   |   |   VignetteSection.qml
|   |       |   |   |   |   |   |   |   VignetteSpecifics.qml
|   |       |   |   |   |   |   |   |   
|   |       |   |   |   |   |   |   +---images
|   |       |   |   |   |   |   |   |       effect.png
|   |       |   |   |   |   |   |   |       effect16.png
|   |       |   |   |   |   |   |   |       effect@2x.png
|   |       |   |   |   |   |   |   |       
|   |       |   |   |   |   |   |   \---source
|   |       |   |   |   |   |   |           effect_template.qml
|   |       |   |   |   |   |   |           
|   |       |   |   |   |   |   \---maps
|   |       |   |   |   |   |           brushnoise.png
|   |       |   |   |   |   |           white.png
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---Helpers
|   |       |   |   |   |   |   |   AxisHelper.qml
|   |       |   |   |   |   |   |   DebugView.qml
|   |       |   |   |   |   |   |   plugins.qmltypes
|   |       |   |   |   |   |   |   qmldir
|   |       |   |   |   |   |   |   qtquick3dhelpersplugin.dll
|   |       |   |   |   |   |   |   WasdController.qml
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---meshes
|   |       |   |   |   |   |           axisGrid.mesh
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---Materials
|   |       |   |   |   |       |   AluminumAnodizedEmissiveMaterial.qml
|   |       |   |   |   |       |   AluminumAnodizedMaterial.qml
|   |       |   |   |   |       |   AluminumBrushedMaterial.qml
|   |       |   |   |   |       |   AluminumEmissiveMaterial.qml
|   |       |   |   |   |       |   AluminumMaterial.qml
|   |       |   |   |   |       |   CopperMaterial.qml
|   |       |   |   |   |       |   FrostedGlassMaterial.qml
|   |       |   |   |   |       |   FrostedGlassSinglePassMaterial.qml
|   |       |   |   |   |       |   GlassMaterial.qml
|   |       |   |   |   |       |   GlassRefractiveMaterial.qml
|   |       |   |   |   |       |   PaperArtisticMaterial.qml
|   |       |   |   |   |       |   PaperOfficeMaterial.qml
|   |       |   |   |   |       |   PlasticStructuredRedEmissiveMaterial.qml
|   |       |   |   |   |       |   PlasticStructuredRedMaterial.qml
|   |       |   |   |   |       |   plugins.qmltypes
|   |       |   |   |   |       |   qmldir
|   |       |   |   |   |       |   qtquick3dmaterialplugin.dll
|   |       |   |   |   |       |   SteelMilledConcentricMaterial.qml
|   |       |   |   |   |       |   
|   |       |   |   |   |       +---designer
|   |       |   |   |   |       |   |   AluminumAnodizedEmissiveMaterialSection.qml
|   |       |   |   |   |       |   |   AluminumAnodizedEmissiveMaterialSpecifics.qml
|   |       |   |   |   |       |   |   AluminumAnodizedMaterialSection.qml
|   |       |   |   |   |       |   |   AluminumAnodizedMaterialSpecifics.qml
|   |       |   |   |   |       |   |   AluminumBrushedMaterialSection.qml
|   |       |   |   |   |       |   |   AluminumBrushedMaterialSpecifics.qml
|   |       |   |   |   |       |   |   AluminumEmissiveMaterialSection.qml
|   |       |   |   |   |       |   |   AluminumEmissiveMaterialSpecifics.qml
|   |       |   |   |   |       |   |   AluminumMaterialSection.qml
|   |       |   |   |   |       |   |   AluminumMaterialSpecifics.qml
|   |       |   |   |   |       |   |   CopperMaterialSection.qml
|   |       |   |   |   |       |   |   CopperMaterialSpecifics.qml
|   |       |   |   |   |       |   |   CustomMaterialSection.qml
|   |       |   |   |   |       |   |   CustomMaterialSpecifics.qml
|   |       |   |   |   |       |   |   FrostedGlassMaterialSection.qml
|   |       |   |   |   |       |   |   FrostedGlassMaterialSpecifics.qml
|   |       |   |   |   |       |   |   FrostedGlassSinglePassMaterialSection.qml
|   |       |   |   |   |       |   |   FrostedGlassSinglePassMaterialSpecifics.qml
|   |       |   |   |   |       |   |   GlassMaterialSection.qml
|   |       |   |   |   |       |   |   GlassMaterialSpecifics.qml
|   |       |   |   |   |       |   |   GlassRefractiveMaterialSection.qml
|   |       |   |   |   |       |   |   GlassRefractiveMaterialSpecifics.qml
|   |       |   |   |   |       |   |   IdComboBox.qml
|   |       |   |   |   |       |   |   materiallib.metainfo
|   |       |   |   |   |       |   |   PaperArtisticMaterialSection.qml
|   |       |   |   |   |       |   |   PaperArtisticMaterialSpecifics.qml
|   |       |   |   |   |       |   |   PaperOfficeMaterialSection.qml
|   |       |   |   |   |       |   |   PaperOfficeMaterialSpecifics.qml
|   |       |   |   |   |       |   |   PlasticStructuredRedEmissiveMaterialSection.qml
|   |       |   |   |   |       |   |   PlasticStructuredRedEmissiveMaterialSpecifics.qml
|   |       |   |   |   |       |   |   PlasticStructuredRedMaterialSection.qml
|   |       |   |   |   |       |   |   PlasticStructuredRedMaterialSpecifics.qml
|   |       |   |   |   |       |   |   SteelMilledConcentricMaterialSection.qml
|   |       |   |   |   |       |   |   SteelMilledConcentricMaterialSpecifics.qml
|   |       |   |   |   |       |   |   
|   |       |   |   |   |       |   +---images
|   |       |   |   |   |       |   |       custommaterial.png
|   |       |   |   |   |       |   |       custommaterial16.png
|   |       |   |   |   |       |   |       custommaterial@2x.png
|   |       |   |   |   |       |   |       
|   |       |   |   |   |       |   \---source
|   |       |   |   |   |       |           custommaterial_template.qml
|   |       |   |   |   |       |           
|   |       |   |   |   |       \---maps
|   |       |   |   |   |               art_paper_normal.png
|   |       |   |   |   |               art_paper_trans.png
|   |       |   |   |   |               brushed_a.png
|   |       |   |   |   |               brushed_full_contrast.png
|   |       |   |   |   |               concentric_milled_steel.png
|   |       |   |   |   |               concentric_milled_steel_aniso.png
|   |       |   |   |   |               emissive.png
|   |       |   |   |   |               emissive_mask.png
|   |       |   |   |   |               grunge_b.png
|   |       |   |   |   |               grunge_d.png
|   |       |   |   |   |               paper_diffuse.png
|   |       |   |   |   |               paper_trans.png
|   |       |   |   |   |               randomGradient1D.png
|   |       |   |   |   |               randomGradient2D.png
|   |       |   |   |   |               randomGradient3D.png
|   |       |   |   |   |               randomGradient4D.png
|   |       |   |   |   |               shadow.png
|   |       |   |   |   |               spherical_checker.png
|   |       |   |   |   |               
|   |       |   |   |   +---QtRemoteObjects
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       qtremoteobjects.dll
|   |       |   |   |   |       
|   |       |   |   |   +---QtSensors
|   |       |   |   |   |       declarative_sensors.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   +---QtTest
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       qmltestplugin.dll
|   |       |   |   |   |       SignalSpy.qml
|   |       |   |   |   |       TestCase.qml
|   |       |   |   |   |       testlogger.js
|   |       |   |   |   |       
|   |       |   |   |   +---QtWebChannel
|   |       |   |   |   |       declarative_webchannel.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   +---QtWebSockets
|   |       |   |   |   |       declarative_qmlwebsockets.dll
|   |       |   |   |   |       plugins.qmltypes
|   |       |   |   |   |       qmldir
|   |       |   |   |   |       
|   |       |   |   |   \---QtWebView
|   |       |   |   |           declarative_webview.dll
|   |       |   |   |           plugins.qmltypes
|   |       |   |   |           qmldir
|   |       |   |   |           
|   |       |   |   +---qsci
|   |       |   |   |   \---api
|   |       |   |   |       \---python
|   |       |   |   |               PyQt5.api
|   |       |   |   |               
|   |       |   |   \---translations
|   |       |   |           qtbase_ar.qm
|   |       |   |           qtbase_bg.qm
|   |       |   |           qtbase_ca.qm
|   |       |   |           qtbase_cs.qm
|   |       |   |           qtbase_da.qm
|   |       |   |           qtbase_de.qm
|   |       |   |           qtbase_en.qm
|   |       |   |           qtbase_es.qm
|   |       |   |           qtbase_fi.qm
|   |       |   |           qtbase_fr.qm
|   |       |   |           qtbase_gd.qm
|   |       |   |           qtbase_he.qm
|   |       |   |           qtbase_hu.qm
|   |       |   |           qtbase_it.qm
|   |       |   |           qtbase_ja.qm
|   |       |   |           qtbase_ko.qm
|   |       |   |           qtbase_lv.qm
|   |       |   |           qtbase_pl.qm
|   |       |   |           qtbase_ru.qm
|   |       |   |           qtbase_sk.qm
|   |       |   |           qtbase_tr.qm
|   |       |   |           qtbase_uk.qm
|   |       |   |           qtbase_zh_TW.qm
|   |       |   |           qtconnectivity_bg.qm
|   |       |   |           qtconnectivity_ca.qm
|   |       |   |           qtconnectivity_da.qm
|   |       |   |           qtconnectivity_de.qm
|   |       |   |           qtconnectivity_en.qm
|   |       |   |           qtconnectivity_es.qm
|   |       |   |           qtconnectivity_hu.qm
|   |       |   |           qtconnectivity_ko.qm
|   |       |   |           qtconnectivity_pl.qm
|   |       |   |           qtconnectivity_ru.qm
|   |       |   |           qtconnectivity_tr.qm
|   |       |   |           qtconnectivity_uk.qm
|   |       |   |           qtdeclarative_bg.qm
|   |       |   |           qtdeclarative_da.qm
|   |       |   |           qtdeclarative_de.qm
|   |       |   |           qtdeclarative_en.qm
|   |       |   |           qtdeclarative_es.qm
|   |       |   |           qtdeclarative_fi.qm
|   |       |   |           qtdeclarative_fr.qm
|   |       |   |           qtdeclarative_hu.qm
|   |       |   |           qtdeclarative_ja.qm
|   |       |   |           qtdeclarative_ko.qm
|   |       |   |           qtdeclarative_lv.qm
|   |       |   |           qtdeclarative_pl.qm
|   |       |   |           qtdeclarative_ru.qm
|   |       |   |           qtdeclarative_sk.qm
|   |       |   |           qtdeclarative_tr.qm
|   |       |   |           qtdeclarative_uk.qm
|   |       |   |           qtlocation_bg.qm
|   |       |   |           qtlocation_ca.qm
|   |       |   |           qtlocation_da.qm
|   |       |   |           qtlocation_de.qm
|   |       |   |           qtlocation_en.qm
|   |       |   |           qtlocation_es.qm
|   |       |   |           qtlocation_fi.qm
|   |       |   |           qtlocation_fr.qm
|   |       |   |           qtlocation_hu.qm
|   |       |   |           qtlocation_ko.qm
|   |       |   |           qtlocation_pl.qm
|   |       |   |           qtlocation_ru.qm
|   |       |   |           qtlocation_tr.qm
|   |       |   |           qtlocation_uk.qm
|   |       |   |           qtmultimedia_ar.qm
|   |       |   |           qtmultimedia_bg.qm
|   |       |   |           qtmultimedia_ca.qm
|   |       |   |           qtmultimedia_cs.qm
|   |       |   |           qtmultimedia_da.qm
|   |       |   |           qtmultimedia_de.qm
|   |       |   |           qtmultimedia_en.qm
|   |       |   |           qtmultimedia_es.qm
|   |       |   |           qtmultimedia_fi.qm
|   |       |   |           qtmultimedia_fr.qm
|   |       |   |           qtmultimedia_hu.qm
|   |       |   |           qtmultimedia_it.qm
|   |       |   |           qtmultimedia_ja.qm
|   |       |   |           qtmultimedia_ko.qm
|   |       |   |           qtmultimedia_pl.qm
|   |       |   |           qtmultimedia_ru.qm
|   |       |   |           qtmultimedia_sk.qm
|   |       |   |           qtmultimedia_tr.qm
|   |       |   |           qtmultimedia_uk.qm
|   |       |   |           qtmultimedia_zh_TW.qm
|   |       |   |           qtquickcontrols2_ar.qm
|   |       |   |           qtquickcontrols2_bg.qm
|   |       |   |           qtquickcontrols2_ca.qm
|   |       |   |           qtquickcontrols2_da.qm
|   |       |   |           qtquickcontrols2_en.qm
|   |       |   |           qtquickcontrols2_hu.qm
|   |       |   |           qtquickcontrols2_ko.qm
|   |       |   |           qtquickcontrols2_tr.qm
|   |       |   |           qtquickcontrols2_uk.qm
|   |       |   |           qtquickcontrols2_zh_TW.qm
|   |       |   |           qtquickcontrols_bg.qm
|   |       |   |           qtquickcontrols_ca.qm
|   |       |   |           qtquickcontrols_da.qm
|   |       |   |           qtquickcontrols_de.qm
|   |       |   |           qtquickcontrols_en.qm
|   |       |   |           qtquickcontrols_fi.qm
|   |       |   |           qtquickcontrols_fr.qm
|   |       |   |           qtquickcontrols_ja.qm
|   |       |   |           qtquickcontrols_ko.qm
|   |       |   |           qtquickcontrols_ru.qm
|   |       |   |           qtquickcontrols_tr.qm
|   |       |   |           qtquickcontrols_uk.qm
|   |       |   |           qtquickcontrols_zh_TW.qm
|   |       |   |           qtserialport_de.qm
|   |       |   |           qtserialport_en.qm
|   |       |   |           qtserialport_es.qm
|   |       |   |           qtserialport_ja.qm
|   |       |   |           qtserialport_ko.qm
|   |       |   |           qtserialport_pl.qm
|   |       |   |           qtserialport_ru.qm
|   |       |   |           qtserialport_uk.qm
|   |       |   |           qtwebsockets_ca.qm
|   |       |   |           qtwebsockets_de.qm
|   |       |   |           qtwebsockets_en.qm
|   |       |   |           qtwebsockets_es.qm
|   |       |   |           qtwebsockets_fr.qm
|   |       |   |           qtwebsockets_ja.qm
|   |       |   |           qtwebsockets_ko.qm
|   |       |   |           qtwebsockets_pl.qm
|   |       |   |           qtwebsockets_ru.qm
|   |       |   |           qtwebsockets_uk.qm
|   |       |   |           qtxmlpatterns_bg.qm
|   |       |   |           qtxmlpatterns_ca.qm
|   |       |   |           qtxmlpatterns_cs.qm
|   |       |   |           qtxmlpatterns_da.qm
|   |       |   |           qtxmlpatterns_de.qm
|   |       |   |           qtxmlpatterns_en.qm
|   |       |   |           qtxmlpatterns_es.qm
|   |       |   |           qtxmlpatterns_fr.qm
|   |       |   |           qtxmlpatterns_hu.qm
|   |       |   |           qtxmlpatterns_it.qm
|   |       |   |           qtxmlpatterns_ja.qm
|   |       |   |           qtxmlpatterns_ko.qm
|   |       |   |           qtxmlpatterns_pl.qm
|   |       |   |           qtxmlpatterns_ru.qm
|   |       |   |           qtxmlpatterns_sk.qm
|   |       |   |           qtxmlpatterns_uk.qm
|   |       |   |           qtxmlpatterns_zh_TW.qm
|   |       |   |           qt_ar.qm
|   |       |   |           qt_bg.qm
|   |       |   |           qt_ca.qm
|   |       |   |           qt_cs.qm
|   |       |   |           qt_da.qm
|   |       |   |           qt_de.qm
|   |       |   |           qt_en.qm
|   |       |   |           qt_es.qm
|   |       |   |           qt_fa.qm
|   |       |   |           qt_fi.qm
|   |       |   |           qt_fr.qm
|   |       |   |           qt_gd.qm
|   |       |   |           qt_gl.qm
|   |       |   |           qt_he.qm
|   |       |   |           qt_help_ar.qm
|   |       |   |           qt_help_bg.qm
|   |       |   |           qt_help_ca.qm
|   |       |   |           qt_help_cs.qm
|   |       |   |           qt_help_da.qm
|   |       |   |           qt_help_de.qm
|   |       |   |           qt_help_en.qm
|   |       |   |           qt_help_es.qm
|   |       |   |           qt_help_fr.qm
|   |       |   |           qt_help_gl.qm
|   |       |   |           qt_help_hu.qm
|   |       |   |           qt_help_it.qm
|   |       |   |           qt_help_ja.qm
|   |       |   |           qt_help_ko.qm
|   |       |   |           qt_help_pl.qm
|   |       |   |           qt_help_ru.qm
|   |       |   |           qt_help_sk.qm
|   |       |   |           qt_help_sl.qm
|   |       |   |           qt_help_tr.qm
|   |       |   |           qt_help_uk.qm
|   |       |   |           qt_help_zh_CN.qm
|   |       |   |           qt_help_zh_TW.qm
|   |       |   |           qt_hu.qm
|   |       |   |           qt_it.qm
|   |       |   |           qt_ja.qm
|   |       |   |           qt_ko.qm
|   |       |   |           qt_lt.qm
|   |       |   |           qt_lv.qm
|   |       |   |           qt_pl.qm
|   |       |   |           qt_pt.qm
|   |       |   |           qt_ru.qm
|   |       |   |           qt_sk.qm
|   |       |   |           qt_sl.qm
|   |       |   |           qt_sv.qm
|   |       |   |           qt_tr.qm
|   |       |   |           qt_uk.qm
|   |       |   |           qt_zh_CN.qm
|   |       |   |           qt_zh_TW.qm
|   |       |   |           
|   |       |   +---uic
|   |       |   |   |   driver.py
|   |       |   |   |   exceptions.py
|   |       |   |   |   icon_cache.py
|   |       |   |   |   objcreator.py
|   |       |   |   |   properties.py
|   |       |   |   |   pyuic.py
|   |       |   |   |   uiparser.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---Compiler
|   |       |   |   |       compiler.py
|   |       |   |   |       indenter.py
|   |       |   |   |       misc.py
|   |       |   |   |       proxy_metaclass.py
|   |       |   |   |       qobjectcreator.py
|   |       |   |   |       qtproxies.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---Loader
|   |       |   |   |       loader.py
|   |       |   |   |       qobjectcreator.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---port_v2
|   |       |   |   |       ascii_upper.py
|   |       |   |   |       as_string.py
|   |       |   |   |       proxy_base.py
|   |       |   |   |       string_io.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---port_v3
|   |       |   |   |       ascii_upper.py
|   |       |   |   |       as_string.py
|   |       |   |   |       proxy_base.py
|   |       |   |   |       string_io.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---widget-plugins
|   |       |   |           qaxcontainer.py
|   |       |   |           qscintilla.py
|   |       |   |           qtcharts.py
|   |       |   |           qtprintsupport.py
|   |       |   |           qtquickwidgets.py
|   |       |   |           qtwebenginewidgets.py
|   |       |   |           qtwebkit.py
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---PyQt5-5.15.11.dist-info
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---PyQt5_Qt5-5.15.2.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---PyQt5_sip-12.17.0.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       
|   |       +---python_dateutil-2.9.0.post0.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       zip-safe
|   |       |       
|   |       +---python_dotenv-1.1.1.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pytz
|   |       |   |   exceptions.py
|   |       |   |   lazy.py
|   |       |   |   reference.py
|   |       |   |   tzfile.py
|   |       |   |   tzinfo.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---zoneinfo
|   |       |   |   |   CET
|   |       |   |   |   CST6CDT
|   |       |   |   |   Cuba
|   |       |   |   |   EET
|   |       |   |   |   Egypt
|   |       |   |   |   Eire
|   |       |   |   |   EST
|   |       |   |   |   EST5EDT
|   |       |   |   |   Factory
|   |       |   |   |   GB
|   |       |   |   |   GB-Eire
|   |       |   |   |   GMT
|   |       |   |   |   GMT+0
|   |       |   |   |   GMT-0
|   |       |   |   |   GMT0
|   |       |   |   |   Greenwich
|   |       |   |   |   Hongkong
|   |       |   |   |   HST
|   |       |   |   |   Iceland
|   |       |   |   |   Iran
|   |       |   |   |   iso3166.tab
|   |       |   |   |   Israel
|   |       |   |   |   Jamaica
|   |       |   |   |   Japan
|   |       |   |   |   Kwajalein
|   |       |   |   |   leapseconds
|   |       |   |   |   Libya
|   |       |   |   |   MET
|   |       |   |   |   MST
|   |       |   |   |   MST7MDT
|   |       |   |   |   Navajo
|   |       |   |   |   NZ
|   |       |   |   |   NZ-CHAT
|   |       |   |   |   Poland
|   |       |   |   |   Portugal
|   |       |   |   |   PRC
|   |       |   |   |   PST8PDT
|   |       |   |   |   ROC
|   |       |   |   |   ROK
|   |       |   |   |   Singapore
|   |       |   |   |   Turkey
|   |       |   |   |   tzdata.zi
|   |       |   |   |   UCT
|   |       |   |   |   Universal
|   |       |   |   |   UTC
|   |       |   |   |   W-SU
|   |       |   |   |   WET
|   |       |   |   |   zone.tab
|   |       |   |   |   zone1970.tab
|   |       |   |   |   zonenow.tab
|   |       |   |   |   Zulu
|   |       |   |   |   
|   |       |   |   +---Africa
|   |       |   |   |       Abidjan
|   |       |   |   |       Accra
|   |       |   |   |       Addis_Ababa
|   |       |   |   |       Algiers
|   |       |   |   |       Asmara
|   |       |   |   |       Asmera
|   |       |   |   |       Bamako
|   |       |   |   |       Bangui
|   |       |   |   |       Banjul
|   |       |   |   |       Bissau
|   |       |   |   |       Blantyre
|   |       |   |   |       Brazzaville
|   |       |   |   |       Bujumbura
|   |       |   |   |       Cairo
|   |       |   |   |       Casablanca
|   |       |   |   |       Ceuta
|   |       |   |   |       Conakry
|   |       |   |   |       Dakar
|   |       |   |   |       Dar_es_Salaam
|   |       |   |   |       Djibouti
|   |       |   |   |       Douala
|   |       |   |   |       El_Aaiun
|   |       |   |   |       Freetown
|   |       |   |   |       Gaborone
|   |       |   |   |       Harare
|   |       |   |   |       Johannesburg
|   |       |   |   |       Juba
|   |       |   |   |       Kampala
|   |       |   |   |       Khartoum
|   |       |   |   |       Kigali
|   |       |   |   |       Kinshasa
|   |       |   |   |       Lagos
|   |       |   |   |       Libreville
|   |       |   |   |       Lome
|   |       |   |   |       Luanda
|   |       |   |   |       Lubumbashi
|   |       |   |   |       Lusaka
|   |       |   |   |       Malabo
|   |       |   |   |       Maputo
|   |       |   |   |       Maseru
|   |       |   |   |       Mbabane
|   |       |   |   |       Mogadishu
|   |       |   |   |       Monrovia
|   |       |   |   |       Nairobi
|   |       |   |   |       Ndjamena
|   |       |   |   |       Niamey
|   |       |   |   |       Nouakchott
|   |       |   |   |       Ouagadougou
|   |       |   |   |       Porto-Novo
|   |       |   |   |       Sao_Tome
|   |       |   |   |       Timbuktu
|   |       |   |   |       Tripoli
|   |       |   |   |       Tunis
|   |       |   |   |       Windhoek
|   |       |   |   |       
|   |       |   |   +---America
|   |       |   |   |   |   Adak
|   |       |   |   |   |   Anchorage
|   |       |   |   |   |   Anguilla
|   |       |   |   |   |   Antigua
|   |       |   |   |   |   Araguaina
|   |       |   |   |   |   Aruba
|   |       |   |   |   |   Asuncion
|   |       |   |   |   |   Atikokan
|   |       |   |   |   |   Atka
|   |       |   |   |   |   Bahia
|   |       |   |   |   |   Bahia_Banderas
|   |       |   |   |   |   Barbados
|   |       |   |   |   |   Belem
|   |       |   |   |   |   Belize
|   |       |   |   |   |   Blanc-Sablon
|   |       |   |   |   |   Boa_Vista
|   |       |   |   |   |   Bogota
|   |       |   |   |   |   Boise
|   |       |   |   |   |   Buenos_Aires
|   |       |   |   |   |   Cambridge_Bay
|   |       |   |   |   |   Campo_Grande
|   |       |   |   |   |   Cancun
|   |       |   |   |   |   Caracas
|   |       |   |   |   |   Catamarca
|   |       |   |   |   |   Cayenne
|   |       |   |   |   |   Cayman
|   |       |   |   |   |   Chicago
|   |       |   |   |   |   Chihuahua
|   |       |   |   |   |   Ciudad_Juarez
|   |       |   |   |   |   Coral_Harbour
|   |       |   |   |   |   Cordoba
|   |       |   |   |   |   Costa_Rica
|   |       |   |   |   |   Coyhaique
|   |       |   |   |   |   Creston
|   |       |   |   |   |   Cuiaba
|   |       |   |   |   |   Curacao
|   |       |   |   |   |   Danmarkshavn
|   |       |   |   |   |   Dawson
|   |       |   |   |   |   Dawson_Creek
|   |       |   |   |   |   Denver
|   |       |   |   |   |   Detroit
|   |       |   |   |   |   Dominica
|   |       |   |   |   |   Edmonton
|   |       |   |   |   |   Eirunepe
|   |       |   |   |   |   El_Salvador
|   |       |   |   |   |   Ensenada
|   |       |   |   |   |   Fortaleza
|   |       |   |   |   |   Fort_Nelson
|   |       |   |   |   |   Fort_Wayne
|   |       |   |   |   |   Glace_Bay
|   |       |   |   |   |   Godthab
|   |       |   |   |   |   Goose_Bay
|   |       |   |   |   |   Grand_Turk
|   |       |   |   |   |   Grenada
|   |       |   |   |   |   Guadeloupe
|   |       |   |   |   |   Guatemala
|   |       |   |   |   |   Guayaquil
|   |       |   |   |   |   Guyana
|   |       |   |   |   |   Halifax
|   |       |   |   |   |   Havana
|   |       |   |   |   |   Hermosillo
|   |       |   |   |   |   Indianapolis
|   |       |   |   |   |   Inuvik
|   |       |   |   |   |   Iqaluit
|   |       |   |   |   |   Jamaica
|   |       |   |   |   |   Jujuy
|   |       |   |   |   |   Juneau
|   |       |   |   |   |   Knox_IN
|   |       |   |   |   |   Kralendijk
|   |       |   |   |   |   La_Paz
|   |       |   |   |   |   Lima
|   |       |   |   |   |   Los_Angeles
|   |       |   |   |   |   Louisville
|   |       |   |   |   |   Lower_Princes
|   |       |   |   |   |   Maceio
|   |       |   |   |   |   Managua
|   |       |   |   |   |   Manaus
|   |       |   |   |   |   Marigot
|   |       |   |   |   |   Martinique
|   |       |   |   |   |   Matamoros
|   |       |   |   |   |   Mazatlan
|   |       |   |   |   |   Mendoza
|   |       |   |   |   |   Menominee
|   |       |   |   |   |   Merida
|   |       |   |   |   |   Metlakatla
|   |       |   |   |   |   Mexico_City
|   |       |   |   |   |   Miquelon
|   |       |   |   |   |   Moncton
|   |       |   |   |   |   Monterrey
|   |       |   |   |   |   Montevideo
|   |       |   |   |   |   Montreal
|   |       |   |   |   |   Montserrat
|   |       |   |   |   |   Nassau
|   |       |   |   |   |   New_York
|   |       |   |   |   |   Nipigon
|   |       |   |   |   |   Nome
|   |       |   |   |   |   Noronha
|   |       |   |   |   |   Nuuk
|   |       |   |   |   |   Ojinaga
|   |       |   |   |   |   Panama
|   |       |   |   |   |   Pangnirtung
|   |       |   |   |   |   Paramaribo
|   |       |   |   |   |   Phoenix
|   |       |   |   |   |   Port-au-Prince
|   |       |   |   |   |   Porto_Acre
|   |       |   |   |   |   Porto_Velho
|   |       |   |   |   |   Port_of_Spain
|   |       |   |   |   |   Puerto_Rico
|   |       |   |   |   |   Punta_Arenas
|   |       |   |   |   |   Rainy_River
|   |       |   |   |   |   Rankin_Inlet
|   |       |   |   |   |   Recife
|   |       |   |   |   |   Regina
|   |       |   |   |   |   Resolute
|   |       |   |   |   |   Rio_Branco
|   |       |   |   |   |   Rosario
|   |       |   |   |   |   Santarem
|   |       |   |   |   |   Santa_Isabel
|   |       |   |   |   |   Santiago
|   |       |   |   |   |   Santo_Domingo
|   |       |   |   |   |   Sao_Paulo
|   |       |   |   |   |   Scoresbysund
|   |       |   |   |   |   Shiprock
|   |       |   |   |   |   Sitka
|   |       |   |   |   |   St_Barthelemy
|   |       |   |   |   |   St_Johns
|   |       |   |   |   |   St_Kitts
|   |       |   |   |   |   St_Lucia
|   |       |   |   |   |   St_Thomas
|   |       |   |   |   |   St_Vincent
|   |       |   |   |   |   Swift_Current
|   |       |   |   |   |   Tegucigalpa
|   |       |   |   |   |   Thule
|   |       |   |   |   |   Thunder_Bay
|   |       |   |   |   |   Tijuana
|   |       |   |   |   |   Toronto
|   |       |   |   |   |   Tortola
|   |       |   |   |   |   Vancouver
|   |       |   |   |   |   Virgin
|   |       |   |   |   |   Whitehorse
|   |       |   |   |   |   Winnipeg
|   |       |   |   |   |   Yakutat
|   |       |   |   |   |   Yellowknife
|   |       |   |   |   |   
|   |       |   |   |   +---Argentina
|   |       |   |   |   |       Buenos_Aires
|   |       |   |   |   |       Catamarca
|   |       |   |   |   |       ComodRivadavia
|   |       |   |   |   |       Cordoba
|   |       |   |   |   |       Jujuy
|   |       |   |   |   |       La_Rioja
|   |       |   |   |   |       Mendoza
|   |       |   |   |   |       Rio_Gallegos
|   |       |   |   |   |       Salta
|   |       |   |   |   |       San_Juan
|   |       |   |   |   |       San_Luis
|   |       |   |   |   |       Tucuman
|   |       |   |   |   |       Ushuaia
|   |       |   |   |   |       
|   |       |   |   |   +---Indiana
|   |       |   |   |   |       Indianapolis
|   |       |   |   |   |       Knox
|   |       |   |   |   |       Marengo
|   |       |   |   |   |       Petersburg
|   |       |   |   |   |       Tell_City
|   |       |   |   |   |       Vevay
|   |       |   |   |   |       Vincennes
|   |       |   |   |   |       Winamac
|   |       |   |   |   |       
|   |       |   |   |   +---Kentucky
|   |       |   |   |   |       Louisville
|   |       |   |   |   |       Monticello
|   |       |   |   |   |       
|   |       |   |   |   \---North_Dakota
|   |       |   |   |           Beulah
|   |       |   |   |           Center
|   |       |   |   |           New_Salem
|   |       |   |   |           
|   |       |   |   +---Antarctica
|   |       |   |   |       Casey
|   |       |   |   |       Davis
|   |       |   |   |       DumontDUrville
|   |       |   |   |       Macquarie
|   |       |   |   |       Mawson
|   |       |   |   |       McMurdo
|   |       |   |   |       Palmer
|   |       |   |   |       Rothera
|   |       |   |   |       South_Pole
|   |       |   |   |       Syowa
|   |       |   |   |       Troll
|   |       |   |   |       Vostok
|   |       |   |   |       
|   |       |   |   +---Arctic
|   |       |   |   |       Longyearbyen
|   |       |   |   |       
|   |       |   |   +---Asia
|   |       |   |   |       Aden
|   |       |   |   |       Almaty
|   |       |   |   |       Amman
|   |       |   |   |       Anadyr
|   |       |   |   |       Aqtau
|   |       |   |   |       Aqtobe
|   |       |   |   |       Ashgabat
|   |       |   |   |       Ashkhabad
|   |       |   |   |       Atyrau
|   |       |   |   |       Baghdad
|   |       |   |   |       Bahrain
|   |       |   |   |       Baku
|   |       |   |   |       Bangkok
|   |       |   |   |       Barnaul
|   |       |   |   |       Beirut
|   |       |   |   |       Bishkek
|   |       |   |   |       Brunei
|   |       |   |   |       Calcutta
|   |       |   |   |       Chita
|   |       |   |   |       Choibalsan
|   |       |   |   |       Chongqing
|   |       |   |   |       Chungking
|   |       |   |   |       Colombo
|   |       |   |   |       Dacca
|   |       |   |   |       Damascus
|   |       |   |   |       Dhaka
|   |       |   |   |       Dili
|   |       |   |   |       Dubai
|   |       |   |   |       Dushanbe
|   |       |   |   |       Famagusta
|   |       |   |   |       Gaza
|   |       |   |   |       Harbin
|   |       |   |   |       Hebron
|   |       |   |   |       Hong_Kong
|   |       |   |   |       Hovd
|   |       |   |   |       Ho_Chi_Minh
|   |       |   |   |       Irkutsk
|   |       |   |   |       Istanbul
|   |       |   |   |       Jakarta
|   |       |   |   |       Jayapura
|   |       |   |   |       Jerusalem
|   |       |   |   |       Kabul
|   |       |   |   |       Kamchatka
|   |       |   |   |       Karachi
|   |       |   |   |       Kashgar
|   |       |   |   |       Kathmandu
|   |       |   |   |       Katmandu
|   |       |   |   |       Khandyga
|   |       |   |   |       Kolkata
|   |       |   |   |       Krasnoyarsk
|   |       |   |   |       Kuala_Lumpur
|   |       |   |   |       Kuching
|   |       |   |   |       Kuwait
|   |       |   |   |       Macao
|   |       |   |   |       Macau
|   |       |   |   |       Magadan
|   |       |   |   |       Makassar
|   |       |   |   |       Manila
|   |       |   |   |       Muscat
|   |       |   |   |       Nicosia
|   |       |   |   |       Novokuznetsk
|   |       |   |   |       Novosibirsk
|   |       |   |   |       Omsk
|   |       |   |   |       Oral
|   |       |   |   |       Phnom_Penh
|   |       |   |   |       Pontianak
|   |       |   |   |       Pyongyang
|   |       |   |   |       Qatar
|   |       |   |   |       Qostanay
|   |       |   |   |       Qyzylorda
|   |       |   |   |       Rangoon
|   |       |   |   |       Riyadh
|   |       |   |   |       Saigon
|   |       |   |   |       Sakhalin
|   |       |   |   |       Samarkand
|   |       |   |   |       Seoul
|   |       |   |   |       Shanghai
|   |       |   |   |       Singapore
|   |       |   |   |       Srednekolymsk
|   |       |   |   |       Taipei
|   |       |   |   |       Tashkent
|   |       |   |   |       Tbilisi
|   |       |   |   |       Tehran
|   |       |   |   |       Tel_Aviv
|   |       |   |   |       Thimbu
|   |       |   |   |       Thimphu
|   |       |   |   |       Tokyo
|   |       |   |   |       Tomsk
|   |       |   |   |       Ujung_Pandang
|   |       |   |   |       Ulaanbaatar
|   |       |   |   |       Ulan_Bator
|   |       |   |   |       Urumqi
|   |       |   |   |       Ust-Nera
|   |       |   |   |       Vientiane
|   |       |   |   |       Vladivostok
|   |       |   |   |       Yakutsk
|   |       |   |   |       Yangon
|   |       |   |   |       Yekaterinburg
|   |       |   |   |       Yerevan
|   |       |   |   |       
|   |       |   |   +---Atlantic
|   |       |   |   |       Azores
|   |       |   |   |       Bermuda
|   |       |   |   |       Canary
|   |       |   |   |       Cape_Verde
|   |       |   |   |       Faeroe
|   |       |   |   |       Faroe
|   |       |   |   |       Jan_Mayen
|   |       |   |   |       Madeira
|   |       |   |   |       Reykjavik
|   |       |   |   |       South_Georgia
|   |       |   |   |       Stanley
|   |       |   |   |       St_Helena
|   |       |   |   |       
|   |       |   |   +---Australia
|   |       |   |   |       ACT
|   |       |   |   |       Adelaide
|   |       |   |   |       Brisbane
|   |       |   |   |       Broken_Hill
|   |       |   |   |       Canberra
|   |       |   |   |       Currie
|   |       |   |   |       Darwin
|   |       |   |   |       Eucla
|   |       |   |   |       Hobart
|   |       |   |   |       LHI
|   |       |   |   |       Lindeman
|   |       |   |   |       Lord_Howe
|   |       |   |   |       Melbourne
|   |       |   |   |       North
|   |       |   |   |       NSW
|   |       |   |   |       Perth
|   |       |   |   |       Queensland
|   |       |   |   |       South
|   |       |   |   |       Sydney
|   |       |   |   |       Tasmania
|   |       |   |   |       Victoria
|   |       |   |   |       West
|   |       |   |   |       Yancowinna
|   |       |   |   |       
|   |       |   |   +---Brazil
|   |       |   |   |       Acre
|   |       |   |   |       DeNoronha
|   |       |   |   |       East
|   |       |   |   |       West
|   |       |   |   |       
|   |       |   |   +---Canada
|   |       |   |   |       Atlantic
|   |       |   |   |       Central
|   |       |   |   |       Eastern
|   |       |   |   |       Mountain
|   |       |   |   |       Newfoundland
|   |       |   |   |       Pacific
|   |       |   |   |       Saskatchewan
|   |       |   |   |       Yukon
|   |       |   |   |       
|   |       |   |   +---Chile
|   |       |   |   |       Continental
|   |       |   |   |       EasterIsland
|   |       |   |   |       
|   |       |   |   +---Etc
|   |       |   |   |       GMT
|   |       |   |   |       GMT+0
|   |       |   |   |       GMT+1
|   |       |   |   |       GMT+10
|   |       |   |   |       GMT+11
|   |       |   |   |       GMT+12
|   |       |   |   |       GMT+2
|   |       |   |   |       GMT+3
|   |       |   |   |       GMT+4
|   |       |   |   |       GMT+5
|   |       |   |   |       GMT+6
|   |       |   |   |       GMT+7
|   |       |   |   |       GMT+8
|   |       |   |   |       GMT+9
|   |       |   |   |       GMT-0
|   |       |   |   |       GMT-1
|   |       |   |   |       GMT-10
|   |       |   |   |       GMT-11
|   |       |   |   |       GMT-12
|   |       |   |   |       GMT-13
|   |       |   |   |       GMT-14
|   |       |   |   |       GMT-2
|   |       |   |   |       GMT-3
|   |       |   |   |       GMT-4
|   |       |   |   |       GMT-5
|   |       |   |   |       GMT-6
|   |       |   |   |       GMT-7
|   |       |   |   |       GMT-8
|   |       |   |   |       GMT-9
|   |       |   |   |       GMT0
|   |       |   |   |       Greenwich
|   |       |   |   |       UCT
|   |       |   |   |       Universal
|   |       |   |   |       UTC
|   |       |   |   |       Zulu
|   |       |   |   |       
|   |       |   |   +---Europe
|   |       |   |   |       Amsterdam
|   |       |   |   |       Andorra
|   |       |   |   |       Astrakhan
|   |       |   |   |       Athens
|   |       |   |   |       Belfast
|   |       |   |   |       Belgrade
|   |       |   |   |       Berlin
|   |       |   |   |       Bratislava
|   |       |   |   |       Brussels
|   |       |   |   |       Bucharest
|   |       |   |   |       Budapest
|   |       |   |   |       Busingen
|   |       |   |   |       Chisinau
|   |       |   |   |       Copenhagen
|   |       |   |   |       Dublin
|   |       |   |   |       Gibraltar
|   |       |   |   |       Guernsey
|   |       |   |   |       Helsinki
|   |       |   |   |       Isle_of_Man
|   |       |   |   |       Istanbul
|   |       |   |   |       Jersey
|   |       |   |   |       Kaliningrad
|   |       |   |   |       Kiev
|   |       |   |   |       Kirov
|   |       |   |   |       Kyiv
|   |       |   |   |       Lisbon
|   |       |   |   |       Ljubljana
|   |       |   |   |       London
|   |       |   |   |       Luxembourg
|   |       |   |   |       Madrid
|   |       |   |   |       Malta
|   |       |   |   |       Mariehamn
|   |       |   |   |       Minsk
|   |       |   |   |       Monaco
|   |       |   |   |       Moscow
|   |       |   |   |       Nicosia
|   |       |   |   |       Oslo
|   |       |   |   |       Paris
|   |       |   |   |       Podgorica
|   |       |   |   |       Prague
|   |       |   |   |       Riga
|   |       |   |   |       Rome
|   |       |   |   |       Samara
|   |       |   |   |       San_Marino
|   |       |   |   |       Sarajevo
|   |       |   |   |       Saratov
|   |       |   |   |       Simferopol
|   |       |   |   |       Skopje
|   |       |   |   |       Sofia
|   |       |   |   |       Stockholm
|   |       |   |   |       Tallinn
|   |       |   |   |       Tirane
|   |       |   |   |       Tiraspol
|   |       |   |   |       Ulyanovsk
|   |       |   |   |       Uzhgorod
|   |       |   |   |       Vaduz
|   |       |   |   |       Vatican
|   |       |   |   |       Vienna
|   |       |   |   |       Vilnius
|   |       |   |   |       Volgograd
|   |       |   |   |       Warsaw
|   |       |   |   |       Zagreb
|   |       |   |   |       Zaporozhye
|   |       |   |   |       Zurich
|   |       |   |   |       
|   |       |   |   +---Indian
|   |       |   |   |       Antananarivo
|   |       |   |   |       Chagos
|   |       |   |   |       Christmas
|   |       |   |   |       Cocos
|   |       |   |   |       Comoro
|   |       |   |   |       Kerguelen
|   |       |   |   |       Mahe
|   |       |   |   |       Maldives
|   |       |   |   |       Mauritius
|   |       |   |   |       Mayotte
|   |       |   |   |       Reunion
|   |       |   |   |       
|   |       |   |   +---Mexico
|   |       |   |   |       BajaNorte
|   |       |   |   |       BajaSur
|   |       |   |   |       General
|   |       |   |   |       
|   |       |   |   +---Pacific
|   |       |   |   |       Apia
|   |       |   |   |       Auckland
|   |       |   |   |       Bougainville
|   |       |   |   |       Chatham
|   |       |   |   |       Chuuk
|   |       |   |   |       Easter
|   |       |   |   |       Efate
|   |       |   |   |       Enderbury
|   |       |   |   |       Fakaofo
|   |       |   |   |       Fiji
|   |       |   |   |       Funafuti
|   |       |   |   |       Galapagos
|   |       |   |   |       Gambier
|   |       |   |   |       Guadalcanal
|   |       |   |   |       Guam
|   |       |   |   |       Honolulu
|   |       |   |   |       Johnston
|   |       |   |   |       Kanton
|   |       |   |   |       Kiritimati
|   |       |   |   |       Kosrae
|   |       |   |   |       Kwajalein
|   |       |   |   |       Majuro
|   |       |   |   |       Marquesas
|   |       |   |   |       Midway
|   |       |   |   |       Nauru
|   |       |   |   |       Niue
|   |       |   |   |       Norfolk
|   |       |   |   |       Noumea
|   |       |   |   |       Pago_Pago
|   |       |   |   |       Palau
|   |       |   |   |       Pitcairn
|   |       |   |   |       Pohnpei
|   |       |   |   |       Ponape
|   |       |   |   |       Port_Moresby
|   |       |   |   |       Rarotonga
|   |       |   |   |       Saipan
|   |       |   |   |       Samoa
|   |       |   |   |       Tahiti
|   |       |   |   |       Tarawa
|   |       |   |   |       Tongatapu
|   |       |   |   |       Truk
|   |       |   |   |       Wake
|   |       |   |   |       Wallis
|   |       |   |   |       Yap
|   |       |   |   |       
|   |       |   |   \---US
|   |       |   |           Alaska
|   |       |   |           Aleutian
|   |       |   |           Arizona
|   |       |   |           Central
|   |       |   |           East-Indiana
|   |       |   |           Eastern
|   |       |   |           Hawaii
|   |       |   |           Indiana-Starke
|   |       |   |           Michigan
|   |       |   |           Mountain
|   |       |   |           Pacific
|   |       |   |           Samoa
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           exceptions.cpython-312.pyc
|   |       |           lazy.cpython-312.pyc
|   |       |           tzfile.cpython-312.pyc
|   |       |           tzinfo.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---pytz-2025.2.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE.txt
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       zip-safe
|   |       |       
|   |       +---reportlab
|   |       |   |   rl_config.py
|   |       |   |   rl_settings.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---fonts
|   |       |   |       00readme.txt
|   |       |   |       bitstream-vera-license.txt
|   |       |   |       callig15.afm
|   |       |   |       callig15.pfb
|   |       |   |       cobo____.pfb
|   |       |   |       cob_____.pfb
|   |       |   |       com_____.pfb
|   |       |   |       coo_____.pfb
|   |       |   |       DarkGarden-changelog.txt
|   |       |   |       DarkGarden-copying-gpl.txt
|   |       |   |       DarkGarden-copying.txt
|   |       |   |       DarkGarden-readme.txt
|   |       |   |       DarkGarden.sfd
|   |       |   |       DarkGardenMK.afm
|   |       |   |       DarkGardenMK.pfb
|   |       |   |       hb-test.ttf
|   |       |   |       sy______.pfb
|   |       |   |       Vera.ttf
|   |       |   |       VeraBd.ttf
|   |       |   |       VeraBI.ttf
|   |       |   |       VeraIt.ttf
|   |       |   |       zd______.pfb
|   |       |   |       zx______.pfb
|   |       |   |       zy______.pfb
|   |       |   |       _abi____.pfb
|   |       |   |       _ab_____.pfb
|   |       |   |       _ai_____.pfb
|   |       |   |       _a______.pfb
|   |       |   |       _ebi____.pfb
|   |       |   |       _eb_____.pfb
|   |       |   |       _ei_____.pfb
|   |       |   |       _er_____.pfb
|   |       |   |       
|   |       |   +---graphics
|   |       |   |   |   renderbase.py
|   |       |   |   |   renderPDF.py
|   |       |   |   |   renderPM.py
|   |       |   |   |   renderPS.py
|   |       |   |   |   renderSVG.py
|   |       |   |   |   shapes.py
|   |       |   |   |   svgpath.py
|   |       |   |   |   testdrawings.py
|   |       |   |   |   testshapes.py
|   |       |   |   |   transform.py
|   |       |   |   |   utils.py
|   |       |   |   |   widgetbase.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---barcode
|   |       |   |   |       code128.py
|   |       |   |   |       code39.py
|   |       |   |   |       code93.py
|   |       |   |   |       common.py
|   |       |   |   |       dmtx.py
|   |       |   |   |       eanbc.py
|   |       |   |   |       ecc200datamatrix.py
|   |       |   |   |       fourstate.py
|   |       |   |   |       lto.py
|   |       |   |   |       qr.py
|   |       |   |   |       qrencoder.py
|   |       |   |   |       test.py
|   |       |   |   |       usps.py
|   |       |   |   |       usps4s.py
|   |       |   |   |       widgets.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---charts
|   |       |   |   |       areas.py
|   |       |   |   |       axes.py
|   |       |   |   |       barcharts.py
|   |       |   |   |       dotbox.py
|   |       |   |   |       doughnut.py
|   |       |   |   |       legends.py
|   |       |   |   |       linecharts.py
|   |       |   |   |       lineplots.py
|   |       |   |   |       markers.py
|   |       |   |   |       piecharts.py
|   |       |   |   |       slidebox.py
|   |       |   |   |       spider.py
|   |       |   |   |       textlabels.py
|   |       |   |   |       utils.py
|   |       |   |   |       utils3d.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   +---samples
|   |       |   |   |       bubble.py
|   |       |   |   |       clustered_bar.py
|   |       |   |   |       clustered_column.py
|   |       |   |   |       excelcolors.py
|   |       |   |   |       exploded_pie.py
|   |       |   |   |       filled_radar.py
|   |       |   |   |       linechart_with_markers.py
|   |       |   |   |       line_chart.py
|   |       |   |   |       radar.py
|   |       |   |   |       runall.py
|   |       |   |   |       scatter.py
|   |       |   |   |       scatter_lines.py
|   |       |   |   |       scatter_lines_markers.py
|   |       |   |   |       simple_pie.py
|   |       |   |   |       stacked_bar.py
|   |       |   |   |       stacked_column.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---widgets
|   |       |   |           adjustableArrow.py
|   |       |   |           eventcal.py
|   |       |   |           flags.py
|   |       |   |           grids.py
|   |       |   |           markers.py
|   |       |   |           signsandsymbols.py
|   |       |   |           table.py
|   |       |   |           __init__.py
|   |       |   |           
|   |       |   +---lib
|   |       |   |   |   abag.py
|   |       |   |   |   arciv.py
|   |       |   |   |   attrmap.py
|   |       |   |   |   boxstuff.py
|   |       |   |   |   codecharts.py
|   |       |   |   |   colors.py
|   |       |   |   |   corp.py
|   |       |   |   |   enums.py
|   |       |   |   |   extformat.py
|   |       |   |   |   fontfinder.py
|   |       |   |   |   fonts.py
|   |       |   |   |   formatters.py
|   |       |   |   |   geomutils.py
|   |       |   |   |   logger.py
|   |       |   |   |   normalDate.py
|   |       |   |   |   pagesizes.py
|   |       |   |   |   pdfencrypt.py
|   |       |   |   |   PyFontify.py
|   |       |   |   |   pygments2xpre.py
|   |       |   |   |   randomtext.py
|   |       |   |   |   rltempfile.py
|   |       |   |   |   rl_accel.py
|   |       |   |   |   rl_safe_eval.py
|   |       |   |   |   rparsexml.py
|   |       |   |   |   sequencer.py
|   |       |   |   |   styles.py
|   |       |   |   |   testutils.py
|   |       |   |   |   textsplit.py
|   |       |   |   |   units.py
|   |       |   |   |   utils.py
|   |       |   |   |   validators.py
|   |       |   |   |   yaml.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           abag.cpython-312.pyc
|   |       |   |           boxstuff.cpython-312.pyc
|   |       |   |           colors.cpython-312.pyc
|   |       |   |           enums.cpython-312.pyc
|   |       |   |           fonts.cpython-312.pyc
|   |       |   |           geomutils.cpython-312.pyc
|   |       |   |           logger.cpython-312.pyc
|   |       |   |           normalDate.cpython-312.pyc
|   |       |   |           pagesizes.cpython-312.pyc
|   |       |   |           PyFontify.cpython-312.pyc
|   |       |   |           rltempfile.cpython-312.pyc
|   |       |   |           rl_accel.cpython-312.pyc
|   |       |   |           rl_safe_eval.cpython-312.pyc
|   |       |   |           sequencer.cpython-312.pyc
|   |       |   |           styles.cpython-312.pyc
|   |       |   |           textsplit.cpython-312.pyc
|   |       |   |           units.cpython-312.pyc
|   |       |   |           utils.cpython-312.pyc
|   |       |   |           validators.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---pdfbase
|   |       |   |   |   acroform.py
|   |       |   |   |   cidfonts.py
|   |       |   |   |   pdfdoc.py
|   |       |   |   |   pdfform.py
|   |       |   |   |   pdfmetrics.py
|   |       |   |   |   pdfpattern.py
|   |       |   |   |   pdfutils.py
|   |       |   |   |   rl_codecs.py
|   |       |   |   |   ttfonts.py
|   |       |   |   |   _can_cmap_data.py
|   |       |   |   |   _cidfontdata.py
|   |       |   |   |   _fontdata.py
|   |       |   |   |   _fontdata_enc_macexpert.py
|   |       |   |   |   _fontdata_enc_macroman.py
|   |       |   |   |   _fontdata_enc_pdfdoc.py
|   |       |   |   |   _fontdata_enc_standard.py
|   |       |   |   |   _fontdata_enc_symbol.py
|   |       |   |   |   _fontdata_enc_winansi.py
|   |       |   |   |   _fontdata_enc_zapfdingbats.py
|   |       |   |   |   _fontdata_widths_courier.py
|   |       |   |   |   _fontdata_widths_courierbold.py
|   |       |   |   |   _fontdata_widths_courierboldoblique.py
|   |       |   |   |   _fontdata_widths_courieroblique.py
|   |       |   |   |   _fontdata_widths_helvetica.py
|   |       |   |   |   _fontdata_widths_helveticabold.py
|   |       |   |   |   _fontdata_widths_helveticaboldoblique.py
|   |       |   |   |   _fontdata_widths_helveticaoblique.py
|   |       |   |   |   _fontdata_widths_symbol.py
|   |       |   |   |   _fontdata_widths_timesbold.py
|   |       |   |   |   _fontdata_widths_timesbolditalic.py
|   |       |   |   |   _fontdata_widths_timesitalic.py
|   |       |   |   |   _fontdata_widths_timesroman.py
|   |       |   |   |   _fontdata_widths_zapfdingbats.py
|   |       |   |   |   _glyphlist.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           pdfdoc.cpython-312.pyc
|   |       |   |           pdfmetrics.cpython-312.pyc
|   |       |   |           pdfutils.cpython-312.pyc
|   |       |   |           rl_codecs.cpython-312.pyc
|   |       |   |           ttfonts.cpython-312.pyc
|   |       |   |           _fontdata.cpython-312.pyc
|   |       |   |           _fontdata_enc_macexpert.cpython-312.pyc
|   |       |   |           _fontdata_enc_macroman.cpython-312.pyc
|   |       |   |           _fontdata_enc_pdfdoc.cpython-312.pyc
|   |       |   |           _fontdata_enc_standard.cpython-312.pyc
|   |       |   |           _fontdata_enc_symbol.cpython-312.pyc
|   |       |   |           _fontdata_enc_winansi.cpython-312.pyc
|   |       |   |           _fontdata_enc_zapfdingbats.cpython-312.pyc
|   |       |   |           _fontdata_widths_courier.cpython-312.pyc
|   |       |   |           _fontdata_widths_courierbold.cpython-312.pyc
|   |       |   |           _fontdata_widths_courierboldoblique.cpython-312.pyc
|   |       |   |           _fontdata_widths_courieroblique.cpython-312.pyc
|   |       |   |           _fontdata_widths_helvetica.cpython-312.pyc
|   |       |   |           _fontdata_widths_helveticabold.cpython-312.pyc
|   |       |   |           _fontdata_widths_helveticaboldoblique.cpython-312.pyc
|   |       |   |           _fontdata_widths_helveticaoblique.cpython-312.pyc
|   |       |   |           _fontdata_widths_symbol.cpython-312.pyc
|   |       |   |           _fontdata_widths_timesbold.cpython-312.pyc
|   |       |   |           _fontdata_widths_timesbolditalic.cpython-312.pyc
|   |       |   |           _fontdata_widths_timesitalic.cpython-312.pyc
|   |       |   |           _fontdata_widths_timesroman.cpython-312.pyc
|   |       |   |           _fontdata_widths_zapfdingbats.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---pdfgen
|   |       |   |   |   canvas.py
|   |       |   |   |   pathobject.py
|   |       |   |   |   pdfgeom.py
|   |       |   |   |   pdfimages.py
|   |       |   |   |   textobject.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           canvas.cpython-312.pyc
|   |       |   |           pathobject.cpython-312.pyc
|   |       |   |           pdfgeom.cpython-312.pyc
|   |       |   |           textobject.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---platypus
|   |       |   |   |   doctemplate.py
|   |       |   |   |   figures.py
|   |       |   |   |   flowables.py
|   |       |   |   |   frames.py
|   |       |   |   |   multicol.py
|   |       |   |   |   para.py
|   |       |   |   |   paragraph.py
|   |       |   |   |   paraparser.py
|   |       |   |   |   tableofcontents.py
|   |       |   |   |   tables.py
|   |       |   |   |   xpreformatted.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           doctemplate.cpython-312.pyc
|   |       |   |           flowables.cpython-312.pyc
|   |       |   |           frames.cpython-312.pyc
|   |       |   |           multicol.cpython-312.pyc
|   |       |   |           paragraph.cpython-312.pyc
|   |       |   |           paraparser.cpython-312.pyc
|   |       |   |           tables.cpython-312.pyc
|   |       |   |           xpreformatted.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           rl_config.cpython-312.pyc
|   |       |           rl_settings.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---reportlab-4.4.3.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---requests
|   |       |   |   adapters.py
|   |       |   |   api.py
|   |       |   |   auth.py
|   |       |   |   certs.py
|   |       |   |   compat.py
|   |       |   |   cookies.py
|   |       |   |   exceptions.py
|   |       |   |   help.py
|   |       |   |   hooks.py
|   |       |   |   models.py
|   |       |   |   packages.py
|   |       |   |   sessions.py
|   |       |   |   status_codes.py
|   |       |   |   structures.py
|   |       |   |   utils.py
|   |       |   |   _internal_utils.py
|   |       |   |   __init__.py
|   |       |   |   __version__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           adapters.cpython-312.pyc
|   |       |           api.cpython-312.pyc
|   |       |           auth.cpython-312.pyc
|   |       |           certs.cpython-312.pyc
|   |       |           compat.cpython-312.pyc
|   |       |           cookies.cpython-312.pyc
|   |       |           exceptions.cpython-312.pyc
|   |       |           hooks.cpython-312.pyc
|   |       |           models.cpython-312.pyc
|   |       |           packages.cpython-312.pyc
|   |       |           sessions.cpython-312.pyc
|   |       |           status_codes.cpython-312.pyc
|   |       |           structures.cpython-312.pyc
|   |       |           utils.cpython-312.pyc
|   |       |           _internal_utils.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           __version__.cpython-312.pyc
|   |       |           
|   |       +---requests-2.32.5.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---six-1.17.0.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       
|   |       +---tzdata
|   |       |   |   zones
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---zoneinfo
|   |       |       |   CET
|   |       |       |   CST6CDT
|   |       |       |   Cuba
|   |       |       |   EET
|   |       |       |   Egypt
|   |       |       |   Eire
|   |       |       |   EST
|   |       |       |   EST5EDT
|   |       |       |   Factory
|   |       |       |   GB
|   |       |       |   GB-Eire
|   |       |       |   GMT
|   |       |       |   GMT+0
|   |       |       |   GMT-0
|   |       |       |   GMT0
|   |       |       |   Greenwich
|   |       |       |   Hongkong
|   |       |       |   HST
|   |       |       |   Iceland
|   |       |       |   Iran
|   |       |       |   iso3166.tab
|   |       |       |   Israel
|   |       |       |   Jamaica
|   |       |       |   Japan
|   |       |       |   Kwajalein
|   |       |       |   leapseconds
|   |       |       |   Libya
|   |       |       |   MET
|   |       |       |   MST
|   |       |       |   MST7MDT
|   |       |       |   Navajo
|   |       |       |   NZ
|   |       |       |   NZ-CHAT
|   |       |       |   Poland
|   |       |       |   Portugal
|   |       |       |   PRC
|   |       |       |   PST8PDT
|   |       |       |   ROC
|   |       |       |   ROK
|   |       |       |   Singapore
|   |       |       |   Turkey
|   |       |       |   tzdata.zi
|   |       |       |   UCT
|   |       |       |   Universal
|   |       |       |   UTC
|   |       |       |   W-SU
|   |       |       |   WET
|   |       |       |   zone.tab
|   |       |       |   zone1970.tab
|   |       |       |   zonenow.tab
|   |       |       |   Zulu
|   |       |       |   __init__.py
|   |       |       |   
|   |       |       +---Africa
|   |       |       |       Abidjan
|   |       |       |       Accra
|   |       |       |       Addis_Ababa
|   |       |       |       Algiers
|   |       |       |       Asmara
|   |       |       |       Asmera
|   |       |       |       Bamako
|   |       |       |       Bangui
|   |       |       |       Banjul
|   |       |       |       Bissau
|   |       |       |       Blantyre
|   |       |       |       Brazzaville
|   |       |       |       Bujumbura
|   |       |       |       Cairo
|   |       |       |       Casablanca
|   |       |       |       Ceuta
|   |       |       |       Conakry
|   |       |       |       Dakar
|   |       |       |       Dar_es_Salaam
|   |       |       |       Djibouti
|   |       |       |       Douala
|   |       |       |       El_Aaiun
|   |       |       |       Freetown
|   |       |       |       Gaborone
|   |       |       |       Harare
|   |       |       |       Johannesburg
|   |       |       |       Juba
|   |       |       |       Kampala
|   |       |       |       Khartoum
|   |       |       |       Kigali
|   |       |       |       Kinshasa
|   |       |       |       Lagos
|   |       |       |       Libreville
|   |       |       |       Lome
|   |       |       |       Luanda
|   |       |       |       Lubumbashi
|   |       |       |       Lusaka
|   |       |       |       Malabo
|   |       |       |       Maputo
|   |       |       |       Maseru
|   |       |       |       Mbabane
|   |       |       |       Mogadishu
|   |       |       |       Monrovia
|   |       |       |       Nairobi
|   |       |       |       Ndjamena
|   |       |       |       Niamey
|   |       |       |       Nouakchott
|   |       |       |       Ouagadougou
|   |       |       |       Porto-Novo
|   |       |       |       Sao_Tome
|   |       |       |       Timbuktu
|   |       |       |       Tripoli
|   |       |       |       Tunis
|   |       |       |       Windhoek
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---America
|   |       |       |   |   Adak
|   |       |       |   |   Anchorage
|   |       |       |   |   Anguilla
|   |       |       |   |   Antigua
|   |       |       |   |   Araguaina
|   |       |       |   |   Aruba
|   |       |       |   |   Asuncion
|   |       |       |   |   Atikokan
|   |       |       |   |   Atka
|   |       |       |   |   Bahia
|   |       |       |   |   Bahia_Banderas
|   |       |       |   |   Barbados
|   |       |       |   |   Belem
|   |       |       |   |   Belize
|   |       |       |   |   Blanc-Sablon
|   |       |       |   |   Boa_Vista
|   |       |       |   |   Bogota
|   |       |       |   |   Boise
|   |       |       |   |   Buenos_Aires
|   |       |       |   |   Cambridge_Bay
|   |       |       |   |   Campo_Grande
|   |       |       |   |   Cancun
|   |       |       |   |   Caracas
|   |       |       |   |   Catamarca
|   |       |       |   |   Cayenne
|   |       |       |   |   Cayman
|   |       |       |   |   Chicago
|   |       |       |   |   Chihuahua
|   |       |       |   |   Ciudad_Juarez
|   |       |       |   |   Coral_Harbour
|   |       |       |   |   Cordoba
|   |       |       |   |   Costa_Rica
|   |       |       |   |   Coyhaique
|   |       |       |   |   Creston
|   |       |       |   |   Cuiaba
|   |       |       |   |   Curacao
|   |       |       |   |   Danmarkshavn
|   |       |       |   |   Dawson
|   |       |       |   |   Dawson_Creek
|   |       |       |   |   Denver
|   |       |       |   |   Detroit
|   |       |       |   |   Dominica
|   |       |       |   |   Edmonton
|   |       |       |   |   Eirunepe
|   |       |       |   |   El_Salvador
|   |       |       |   |   Ensenada
|   |       |       |   |   Fortaleza
|   |       |       |   |   Fort_Nelson
|   |       |       |   |   Fort_Wayne
|   |       |       |   |   Glace_Bay
|   |       |       |   |   Godthab
|   |       |       |   |   Goose_Bay
|   |       |       |   |   Grand_Turk
|   |       |       |   |   Grenada
|   |       |       |   |   Guadeloupe
|   |       |       |   |   Guatemala
|   |       |       |   |   Guayaquil
|   |       |       |   |   Guyana
|   |       |       |   |   Halifax
|   |       |       |   |   Havana
|   |       |       |   |   Hermosillo
|   |       |       |   |   Indianapolis
|   |       |       |   |   Inuvik
|   |       |       |   |   Iqaluit
|   |       |       |   |   Jamaica
|   |       |       |   |   Jujuy
|   |       |       |   |   Juneau
|   |       |       |   |   Knox_IN
|   |       |       |   |   Kralendijk
|   |       |       |   |   La_Paz
|   |       |       |   |   Lima
|   |       |       |   |   Los_Angeles
|   |       |       |   |   Louisville
|   |       |       |   |   Lower_Princes
|   |       |       |   |   Maceio
|   |       |       |   |   Managua
|   |       |       |   |   Manaus
|   |       |       |   |   Marigot
|   |       |       |   |   Martinique
|   |       |       |   |   Matamoros
|   |       |       |   |   Mazatlan
|   |       |       |   |   Mendoza
|   |       |       |   |   Menominee
|   |       |       |   |   Merida
|   |       |       |   |   Metlakatla
|   |       |       |   |   Mexico_City
|   |       |       |   |   Miquelon
|   |       |       |   |   Moncton
|   |       |       |   |   Monterrey
|   |       |       |   |   Montevideo
|   |       |       |   |   Montreal
|   |       |       |   |   Montserrat
|   |       |       |   |   Nassau
|   |       |       |   |   New_York
|   |       |       |   |   Nipigon
|   |       |       |   |   Nome
|   |       |       |   |   Noronha
|   |       |       |   |   Nuuk
|   |       |       |   |   Ojinaga
|   |       |       |   |   Panama
|   |       |       |   |   Pangnirtung
|   |       |       |   |   Paramaribo
|   |       |       |   |   Phoenix
|   |       |       |   |   Port-au-Prince
|   |       |       |   |   Porto_Acre
|   |       |       |   |   Porto_Velho
|   |       |       |   |   Port_of_Spain
|   |       |       |   |   Puerto_Rico
|   |       |       |   |   Punta_Arenas
|   |       |       |   |   Rainy_River
|   |       |       |   |   Rankin_Inlet
|   |       |       |   |   Recife
|   |       |       |   |   Regina
|   |       |       |   |   Resolute
|   |       |       |   |   Rio_Branco
|   |       |       |   |   Rosario
|   |       |       |   |   Santarem
|   |       |       |   |   Santa_Isabel
|   |       |       |   |   Santiago
|   |       |       |   |   Santo_Domingo
|   |       |       |   |   Sao_Paulo
|   |       |       |   |   Scoresbysund
|   |       |       |   |   Shiprock
|   |       |       |   |   Sitka
|   |       |       |   |   St_Barthelemy
|   |       |       |   |   St_Johns
|   |       |       |   |   St_Kitts
|   |       |       |   |   St_Lucia
|   |       |       |   |   St_Thomas
|   |       |       |   |   St_Vincent
|   |       |       |   |   Swift_Current
|   |       |       |   |   Tegucigalpa
|   |       |       |   |   Thule
|   |       |       |   |   Thunder_Bay
|   |       |       |   |   Tijuana
|   |       |       |   |   Toronto
|   |       |       |   |   Tortola
|   |       |       |   |   Vancouver
|   |       |       |   |   Virgin
|   |       |       |   |   Whitehorse
|   |       |       |   |   Winnipeg
|   |       |       |   |   Yakutat
|   |       |       |   |   Yellowknife
|   |       |       |   |   __init__.py
|   |       |       |   |   
|   |       |       |   +---Argentina
|   |       |       |   |       Buenos_Aires
|   |       |       |   |       Catamarca
|   |       |       |   |       ComodRivadavia
|   |       |       |   |       Cordoba
|   |       |       |   |       Jujuy
|   |       |       |   |       La_Rioja
|   |       |       |   |       Mendoza
|   |       |       |   |       Rio_Gallegos
|   |       |       |   |       Salta
|   |       |       |   |       San_Juan
|   |       |       |   |       San_Luis
|   |       |       |   |       Tucuman
|   |       |       |   |       Ushuaia
|   |       |       |   |       __init__.py
|   |       |       |   |       
|   |       |       |   +---Indiana
|   |       |       |   |       Indianapolis
|   |       |       |   |       Knox
|   |       |       |   |       Marengo
|   |       |       |   |       Petersburg
|   |       |       |   |       Tell_City
|   |       |       |   |       Vevay
|   |       |       |   |       Vincennes
|   |       |       |   |       Winamac
|   |       |       |   |       __init__.py
|   |       |       |   |       
|   |       |       |   +---Kentucky
|   |       |       |   |       Louisville
|   |       |       |   |       Monticello
|   |       |       |   |       __init__.py
|   |       |       |   |       
|   |       |       |   \---North_Dakota
|   |       |       |           Beulah
|   |       |       |           Center
|   |       |       |           New_Salem
|   |       |       |           __init__.py
|   |       |       |           
|   |       |       +---Antarctica
|   |       |       |       Casey
|   |       |       |       Davis
|   |       |       |       DumontDUrville
|   |       |       |       Macquarie
|   |       |       |       Mawson
|   |       |       |       McMurdo
|   |       |       |       Palmer
|   |       |       |       Rothera
|   |       |       |       South_Pole
|   |       |       |       Syowa
|   |       |       |       Troll
|   |       |       |       Vostok
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Arctic
|   |       |       |       Longyearbyen
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Asia
|   |       |       |       Aden
|   |       |       |       Almaty
|   |       |       |       Amman
|   |       |       |       Anadyr
|   |       |       |       Aqtau
|   |       |       |       Aqtobe
|   |       |       |       Ashgabat
|   |       |       |       Ashkhabad
|   |       |       |       Atyrau
|   |       |       |       Baghdad
|   |       |       |       Bahrain
|   |       |       |       Baku
|   |       |       |       Bangkok
|   |       |       |       Barnaul
|   |       |       |       Beirut
|   |       |       |       Bishkek
|   |       |       |       Brunei
|   |       |       |       Calcutta
|   |       |       |       Chita
|   |       |       |       Choibalsan
|   |       |       |       Chongqing
|   |       |       |       Chungking
|   |       |       |       Colombo
|   |       |       |       Dacca
|   |       |       |       Damascus
|   |       |       |       Dhaka
|   |       |       |       Dili
|   |       |       |       Dubai
|   |       |       |       Dushanbe
|   |       |       |       Famagusta
|   |       |       |       Gaza
|   |       |       |       Harbin
|   |       |       |       Hebron
|   |       |       |       Hong_Kong
|   |       |       |       Hovd
|   |       |       |       Ho_Chi_Minh
|   |       |       |       Irkutsk
|   |       |       |       Istanbul
|   |       |       |       Jakarta
|   |       |       |       Jayapura
|   |       |       |       Jerusalem
|   |       |       |       Kabul
|   |       |       |       Kamchatka
|   |       |       |       Karachi
|   |       |       |       Kashgar
|   |       |       |       Kathmandu
|   |       |       |       Katmandu
|   |       |       |       Khandyga
|   |       |       |       Kolkata
|   |       |       |       Krasnoyarsk
|   |       |       |       Kuala_Lumpur
|   |       |       |       Kuching
|   |       |       |       Kuwait
|   |       |       |       Macao
|   |       |       |       Macau
|   |       |       |       Magadan
|   |       |       |       Makassar
|   |       |       |       Manila
|   |       |       |       Muscat
|   |       |       |       Nicosia
|   |       |       |       Novokuznetsk
|   |       |       |       Novosibirsk
|   |       |       |       Omsk
|   |       |       |       Oral
|   |       |       |       Phnom_Penh
|   |       |       |       Pontianak
|   |       |       |       Pyongyang
|   |       |       |       Qatar
|   |       |       |       Qostanay
|   |       |       |       Qyzylorda
|   |       |       |       Rangoon
|   |       |       |       Riyadh
|   |       |       |       Saigon
|   |       |       |       Sakhalin
|   |       |       |       Samarkand
|   |       |       |       Seoul
|   |       |       |       Shanghai
|   |       |       |       Singapore
|   |       |       |       Srednekolymsk
|   |       |       |       Taipei
|   |       |       |       Tashkent
|   |       |       |       Tbilisi
|   |       |       |       Tehran
|   |       |       |       Tel_Aviv
|   |       |       |       Thimbu
|   |       |       |       Thimphu
|   |       |       |       Tokyo
|   |       |       |       Tomsk
|   |       |       |       Ujung_Pandang
|   |       |       |       Ulaanbaatar
|   |       |       |       Ulan_Bator
|   |       |       |       Urumqi
|   |       |       |       Ust-Nera
|   |       |       |       Vientiane
|   |       |       |       Vladivostok
|   |       |       |       Yakutsk
|   |       |       |       Yangon
|   |       |       |       Yekaterinburg
|   |       |       |       Yerevan
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Atlantic
|   |       |       |       Azores
|   |       |       |       Bermuda
|   |       |       |       Canary
|   |       |       |       Cape_Verde
|   |       |       |       Faeroe
|   |       |       |       Faroe
|   |       |       |       Jan_Mayen
|   |       |       |       Madeira
|   |       |       |       Reykjavik
|   |       |       |       South_Georgia
|   |       |       |       Stanley
|   |       |       |       St_Helena
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Australia
|   |       |       |       ACT
|   |       |       |       Adelaide
|   |       |       |       Brisbane
|   |       |       |       Broken_Hill
|   |       |       |       Canberra
|   |       |       |       Currie
|   |       |       |       Darwin
|   |       |       |       Eucla
|   |       |       |       Hobart
|   |       |       |       LHI
|   |       |       |       Lindeman
|   |       |       |       Lord_Howe
|   |       |       |       Melbourne
|   |       |       |       North
|   |       |       |       NSW
|   |       |       |       Perth
|   |       |       |       Queensland
|   |       |       |       South
|   |       |       |       Sydney
|   |       |       |       Tasmania
|   |       |       |       Victoria
|   |       |       |       West
|   |       |       |       Yancowinna
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Brazil
|   |       |       |       Acre
|   |       |       |       DeNoronha
|   |       |       |       East
|   |       |       |       West
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Canada
|   |       |       |       Atlantic
|   |       |       |       Central
|   |       |       |       Eastern
|   |       |       |       Mountain
|   |       |       |       Newfoundland
|   |       |       |       Pacific
|   |       |       |       Saskatchewan
|   |       |       |       Yukon
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Chile
|   |       |       |       Continental
|   |       |       |       EasterIsland
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Etc
|   |       |       |       GMT
|   |       |       |       GMT+0
|   |       |       |       GMT+1
|   |       |       |       GMT+10
|   |       |       |       GMT+11
|   |       |       |       GMT+12
|   |       |       |       GMT+2
|   |       |       |       GMT+3
|   |       |       |       GMT+4
|   |       |       |       GMT+5
|   |       |       |       GMT+6
|   |       |       |       GMT+7
|   |       |       |       GMT+8
|   |       |       |       GMT+9
|   |       |       |       GMT-0
|   |       |       |       GMT-1
|   |       |       |       GMT-10
|   |       |       |       GMT-11
|   |       |       |       GMT-12
|   |       |       |       GMT-13
|   |       |       |       GMT-14
|   |       |       |       GMT-2
|   |       |       |       GMT-3
|   |       |       |       GMT-4
|   |       |       |       GMT-5
|   |       |       |       GMT-6
|   |       |       |       GMT-7
|   |       |       |       GMT-8
|   |       |       |       GMT-9
|   |       |       |       GMT0
|   |       |       |       Greenwich
|   |       |       |       UCT
|   |       |       |       Universal
|   |       |       |       UTC
|   |       |       |       Zulu
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Europe
|   |       |       |       Amsterdam
|   |       |       |       Andorra
|   |       |       |       Astrakhan
|   |       |       |       Athens
|   |       |       |       Belfast
|   |       |       |       Belgrade
|   |       |       |       Berlin
|   |       |       |       Bratislava
|   |       |       |       Brussels
|   |       |       |       Bucharest
|   |       |       |       Budapest
|   |       |       |       Busingen
|   |       |       |       Chisinau
|   |       |       |       Copenhagen
|   |       |       |       Dublin
|   |       |       |       Gibraltar
|   |       |       |       Guernsey
|   |       |       |       Helsinki
|   |       |       |       Isle_of_Man
|   |       |       |       Istanbul
|   |       |       |       Jersey
|   |       |       |       Kaliningrad
|   |       |       |       Kiev
|   |       |       |       Kirov
|   |       |       |       Kyiv
|   |       |       |       Lisbon
|   |       |       |       Ljubljana
|   |       |       |       London
|   |       |       |       Luxembourg
|   |       |       |       Madrid
|   |       |       |       Malta
|   |       |       |       Mariehamn
|   |       |       |       Minsk
|   |       |       |       Monaco
|   |       |       |       Moscow
|   |       |       |       Nicosia
|   |       |       |       Oslo
|   |       |       |       Paris
|   |       |       |       Podgorica
|   |       |       |       Prague
|   |       |       |       Riga
|   |       |       |       Rome
|   |       |       |       Samara
|   |       |       |       San_Marino
|   |       |       |       Sarajevo
|   |       |       |       Saratov
|   |       |       |       Simferopol
|   |       |       |       Skopje
|   |       |       |       Sofia
|   |       |       |       Stockholm
|   |       |       |       Tallinn
|   |       |       |       Tirane
|   |       |       |       Tiraspol
|   |       |       |       Ulyanovsk
|   |       |       |       Uzhgorod
|   |       |       |       Vaduz
|   |       |       |       Vatican
|   |       |       |       Vienna
|   |       |       |       Vilnius
|   |       |       |       Volgograd
|   |       |       |       Warsaw
|   |       |       |       Zagreb
|   |       |       |       Zaporozhye
|   |       |       |       Zurich
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Indian
|   |       |       |       Antananarivo
|   |       |       |       Chagos
|   |       |       |       Christmas
|   |       |       |       Cocos
|   |       |       |       Comoro
|   |       |       |       Kerguelen
|   |       |       |       Mahe
|   |       |       |       Maldives
|   |       |       |       Mauritius
|   |       |       |       Mayotte
|   |       |       |       Reunion
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Mexico
|   |       |       |       BajaNorte
|   |       |       |       BajaSur
|   |       |       |       General
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       +---Pacific
|   |       |       |       Apia
|   |       |       |       Auckland
|   |       |       |       Bougainville
|   |       |       |       Chatham
|   |       |       |       Chuuk
|   |       |       |       Easter
|   |       |       |       Efate
|   |       |       |       Enderbury
|   |       |       |       Fakaofo
|   |       |       |       Fiji
|   |       |       |       Funafuti
|   |       |       |       Galapagos
|   |       |       |       Gambier
|   |       |       |       Guadalcanal
|   |       |       |       Guam
|   |       |       |       Honolulu
|   |       |       |       Johnston
|   |       |       |       Kanton
|   |       |       |       Kiritimati
|   |       |       |       Kosrae
|   |       |       |       Kwajalein
|   |       |       |       Majuro
|   |       |       |       Marquesas
|   |       |       |       Midway
|   |       |       |       Nauru
|   |       |       |       Niue
|   |       |       |       Norfolk
|   |       |       |       Noumea
|   |       |       |       Pago_Pago
|   |       |       |       Palau
|   |       |       |       Pitcairn
|   |       |       |       Pohnpei
|   |       |       |       Ponape
|   |       |       |       Port_Moresby
|   |       |       |       Rarotonga
|   |       |       |       Saipan
|   |       |       |       Samoa
|   |       |       |       Tahiti
|   |       |       |       Tarawa
|   |       |       |       Tongatapu
|   |       |       |       Truk
|   |       |       |       Wake
|   |       |       |       Wallis
|   |       |       |       Yap
|   |       |       |       __init__.py
|   |       |       |       
|   |       |       \---US
|   |       |               Alaska
|   |       |               Aleutian
|   |       |               Arizona
|   |       |               Central
|   |       |               East-Indiana
|   |       |               Eastern
|   |       |               Hawaii
|   |       |               Indiana-Starke
|   |       |               Michigan
|   |       |               Mountain
|   |       |               Pacific
|   |       |               Samoa
|   |       |               __init__.py
|   |       |               
|   |       +---tzdata-2025.2.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |       |   LICENSE
|   |       |       |   
|   |       |       \---licenses
|   |       |               LICENSE_APACHE
|   |       |               
|   |       +---urllib3
|   |       |   |   connection.py
|   |       |   |   connectionpool.py
|   |       |   |   exceptions.py
|   |       |   |   fields.py
|   |       |   |   filepost.py
|   |       |   |   poolmanager.py
|   |       |   |   py.typed
|   |       |   |   response.py
|   |       |   |   _base_connection.py
|   |       |   |   _collections.py
|   |       |   |   _request_methods.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---contrib
|   |       |   |   |   pyopenssl.py
|   |       |   |   |   socks.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---emscripten
|   |       |   |   |       connection.py
|   |       |   |   |       emscripten_fetch_worker.js
|   |       |   |   |       fetch.py
|   |       |   |   |       request.py
|   |       |   |   |       response.py
|   |       |   |   |       __init__.py
|   |       |   |   |       
|   |       |   |   \---__pycache__
|   |       |   |           socks.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---http2
|   |       |   |   |   connection.py
|   |       |   |   |   probe.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           probe.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   +---util
|   |       |   |   |   connection.py
|   |       |   |   |   proxy.py
|   |       |   |   |   request.py
|   |       |   |   |   response.py
|   |       |   |   |   retry.py
|   |       |   |   |   ssltransport.py
|   |       |   |   |   ssl_.py
|   |       |   |   |   ssl_match_hostname.py
|   |       |   |   |   timeout.py
|   |       |   |   |   url.py
|   |       |   |   |   util.py
|   |       |   |   |   wait.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           connection.cpython-312.pyc
|   |       |   |           proxy.cpython-312.pyc
|   |       |   |           request.cpython-312.pyc
|   |       |   |           response.cpython-312.pyc
|   |       |   |           retry.cpython-312.pyc
|   |       |   |           ssltransport.cpython-312.pyc
|   |       |   |           ssl_.cpython-312.pyc
|   |       |   |           ssl_match_hostname.cpython-312.pyc
|   |       |   |           timeout.cpython-312.pyc
|   |       |   |           url.cpython-312.pyc
|   |       |   |           util.cpython-312.pyc
|   |       |   |           wait.cpython-312.pyc
|   |       |   |           __init__.cpython-312.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           connection.cpython-312.pyc
|   |       |           connectionpool.cpython-312.pyc
|   |       |           exceptions.cpython-312.pyc
|   |       |           fields.cpython-312.pyc
|   |       |           filepost.cpython-312.pyc
|   |       |           poolmanager.cpython-312.pyc
|   |       |           response.cpython-312.pyc
|   |       |           _base_connection.cpython-312.pyc
|   |       |           _collections.cpython-312.pyc
|   |       |           _request_methods.cpython-312.pyc
|   |       |           _version.cpython-312.pyc
|   |       |           __init__.cpython-312.pyc
|   |       |           
|   |       +---urllib3-2.5.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       \---__pycache__
|   |               six.cpython-312.pyc
|   |               
|   +---Scripts
|   |       activate
|   |       activate.bat
|   |       activate.csh
|   |       activate.fish
|   |       activate.nu
|   |       activate.ps1
|   |       activate.xsh
|   |       activate_this.py
|   |       deactivate.bat
|   |       dotenv.exe
|   |       f2py.exe
|   |       fonttools.exe
|   |       normalizer.exe
|   |       numpy-config.exe
|   |       pydoc.bat
|   |       pyftmerge.exe
|   |       pyftsubset.exe
|   |       pylupdate5.exe
|   |       pyrcc5.exe
|   |       python.exe
|   |       pythonw.exe
|   |       pyuic5.exe
|   |       ttx.exe
|   |       
|   \---share
|       \---man
|           \---man1
|                   ttx.1
|                   
\---__pycache__
        analysis.cpython-312.pyc
        api.cpython-312.pyc
        api.cpython-313.pyc
        pdf_exporter.cpython-312.pyc
        
